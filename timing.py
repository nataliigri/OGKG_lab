import matplotlib.pyplot as plt
import time

# Загрузка функцій з файлу
from main import Point, generate_random_points, largest_triangle
from convexHull import convexHull

# Створення списку обсягів даних
data_sizes = [10, 50, 100, 500, 700, 1000]

# Створення пустого словника для зберігання часів виконання
execution_times = {}

# Цикл для обчислення часу виконання на різних обсягах даних
for size in data_sizes:
    # Генерація випадкових точок
    input_points = generate_random_points(size)
    points = [Point(x, y) for x, y in input_points]

    # Вимірювання часу виконання алгоритму
    start_time = time.time()
    convex_hull_points = convexHull(points)
    largest_triangle_points = largest_triangle(convex_hull_points)
    end_time = time.time()

    # Зберігання часу виконання у словнику
    execution_times[size] = end_time - start_time

# Виведення результатів
for size, execution_time in execution_times.items():
    print(f"Час виконання для обсягу даних {size}: {execution_time} секунд")

# Побудова графіка
plt.plot(data_sizes, list(execution_times.values()), marker='o')
plt.xlabel('Обсяг даних')
plt.ylabel('Час виконання (секунди)')
plt.title('Графік залежності часу виконання від кількості вхідних точок')
plt.xticks(data_sizes)  # Встановлюємо мітки на осі X
plt.grid(True)  # Включаємо сітку
plt.show()
