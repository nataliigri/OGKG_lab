import math

# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
	val = ((q.y - p.y) * (r.x - q.x) -
		(q.x - p.x) * (r.y - q.y))
	if val == 0:
		return 0 # collinear
	elif val > 0:
		return 1 # clock wise
	else:
		return 2 # counterclock wise

# Build convex hull of a set of n points.
def convexHull(points):
    # Find the bottommost point
    ymin = points[0].y
    min_idx = 0
    for i in range(1, len(points)):
        y = points[i].y
        # Pick the bottom-most or choose the leftmost point in case of tie
        if y < ymin or (y == ymin and points[i].x < points[min_idx].x):
            ymin = y
            min_idx = i

    # Place the bottom-most point at the beginning of the list
    points[0], points[min_idx] = points[min_idx], points[0]

    # Sort points based on polar angle with respect to the bottom-most point
    sorted_points = sorted(points[1:], key=lambda p: math.atan2(p.y - points[0].y, p.x - points[0].x))

    # Initialize the convex hull with the first two sorted points
    hull = [points[0], sorted_points[0], sorted_points[1]]

    # Compute the convex hull
    for i in range(2, len(sorted_points)):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])

    # Return the points in the convex hull
    return hull
