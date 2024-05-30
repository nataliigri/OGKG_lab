import matplotlib.pyplot as plt
import random
import math
from convexHull import convexHull

# A class used to store the x and y coordinates of points
class Point:
	def __init__(self, x = None, y = None):
		self.x = x
		self.y = y

# A global point needed for sorting points with reference
# to the first point
p0 = Point(0, 0)

def generate_random_points(num_points):
    # Генеруємо випадкові координати для num_points точок
    points = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(num_points)]
    return points

#Finding a Largest triangle
def largest_triangle(P):
    # Input: P = p0, p1, ..., pn: convex polygon
    # Output: T = pa, pb, pc: largest P-aligned triangle
    
    # Base case: if P has only 3 points, return P as the largest triangle
    if len(P) == 3:
        return P
    
    # Arbitrarily choose a vertex a from P
    a = P[0]
    
    # Find the largest-area triangle Ta rooted at a
    Ta = largest_area_triangle(a, P)
    
    # Find the median point m on the largest interval on P between two vertices of Ta
    m = find_median_point(Ta, P)
    
    # Find the largest-area triangle Tm rooted at m
    Tm = largest_area_triangle(m, P)
    
    # Construct sub-polygons P' and P'' by interleaving intervals using Ta and Tm
    P_prime, P_double_prime = construct_sub_polygons(P, Ta, Tm)
    
    # Recursively find the largest triangle in P' or P'' depending on conditions
    if len(P_prime) > 3:
        return largest_triangle(P_prime)
    elif len(P_double_prime) > 3:
        return largest_triangle(P_double_prime)
    else:
        # No triangle larger than the base case triangles, return the base case triangles
        return [Tm]

def largest_area_triangle(root, points):
    # Input: root = root vertex of triangle, points = list of points
    # Output: largest triangle rooted at root among points
    
    max_area = 0
    result_triangle = None
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                area = abs((points[i].x*(points[j].y-points[k].y) + 
                            points[j].x*(points[k].y-points[i].y) + 
                            points[k].x*(points[i].y-points[j].y)) / 2)
                if area > max_area and points[i] != root and points[j] != root and points[k] != root:
                    max_area = area
                    result_triangle = [points[i], points[j], points[k]]
    
    return result_triangle

def find_median_point(T, points):
    # Input: T = triangle, points = list of points
    # Output: median point on largest interval in T among points
    
    def distance_sq(p1, p2):
        return (p1.x - p2.x)**2 + (p1.y - p2.y)**2
    
    max_distance_sq = 0
    median_point = None
    
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            mid_x = (T[i].x + T[j].x) / 2
            mid_y = (T[i].y + T[j].y) / 2
            mid_point = Point(mid_x, mid_y)
            distance = max(distance_sq(mid_point, point) for point in points)
            if distance > max_distance_sq:
                max_distance_sq = distance
                median_point = mid_point
    
    return median_point

def construct_sub_polygons(points, Ta, Tm):
    # Input: points = list of points, Ta = triangle, Tm = triangle
    # Output: sub-polygons P' and P'' constructed by interleaving intervals using Ta and Tm
    
    def are_interleaving_intervals(a, b, c, d):
        return (a < b < c < d) or (c < d < a < b)
    
    P_prime = []
    P_double_prime = []
    
    for i in range(len(points)):
        if are_interleaving_intervals(Ta[0].x, Ta[1].x, Tm[0].x, Tm[1].x):
            P_prime.append(points[i])
        elif are_interleaving_intervals(Ta[2].x, Ta[0].x, Tm[2].x, Tm[0].x):
            P_double_prime.append(points[i])
    
    return P_prime, P_double_prime

def are_interleaving(Ta, Tm):
    # Input: Ta = triangle, Tm = triangle
    # Output: True if Ta and Tm are interleaving, False otherwise
    
    x_values_ta = [point.x for point in Ta]
    x_values_tm = [point.x for point in Tm]
    
    return (max(x_values_ta) < min(x_values_tm)) or (max(x_values_tm) < min(x_values_ta))

# Define a function to plot points, convex hull, and largest triangle
def plot_points_hull_triangle(points, convex_hull, largest_triangle):
    # Extract x and y coordinates for plotting
    x_points = [point.x for point in points]
    y_points = [point.y for point in points]
    x_convex_hull = [point.x for point in convex_hull]
    y_convex_hull = [point.y for point in convex_hull]
    # Extract x and y coordinates of the largest triangle
    x_triangle = [point.x for point in largest_triangle[0]]  # Access the points of the largest triangle
    y_triangle = [point.y for point in largest_triangle[0]]

    # Plot points
    plt.scatter(x_points, y_points, color='blue', label='Points')

    # Plot convex hull
    plt.plot(x_convex_hull + [x_convex_hull[0]], y_convex_hull + [y_convex_hull[0]], color='green', label='Convex Hull')

    # Plot largest triangle
    plt.plot(x_triangle + [x_triangle[0]], y_triangle + [y_triangle[0]], color='red', label='Largest Triangle')

    # Mark vertices of largest triangle
    for i, txt in enumerate(['A', 'B', 'C']):
        plt.annotate(txt, (x_triangle[i], y_triangle[i]), fontsize=12)

    # Set plot labels and legend
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Convex Hull and Largest Area Triangle')
    plt.legend()

    # Show the plot
    plt.show()

# Testing
input_points = generate_random_points(10)
points = [Point(x, y) for x, y in input_points]
convex_hull_points = convexHull(points)
for point in convex_hull_points:
    print(f"({point.x}, {point.y})")
example = [Point(0, 1), Point(0, 4), Point(1, 8), Point(2, 10), Point(5, 9), Point(9, 0)]
result = largest_triangle(convex_hull_points)
for triangle in result:
    print(f"Largest Triangle: ({triangle[0].x}, {triangle[0].y}), ({triangle[1].x}, {triangle[1].y}), ({triangle[2].x}, {triangle[2].y})")
plot_points_hull_triangle(points, convex_hull_points, result)
#plot_points_hull_triangle(example, example, result)
