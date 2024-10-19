import math

# Ввод значений a, b, x1, xn и Δx
a = float(input("Введите значение a -> "))
b = float(input("Введите значение b -> "))
x1 = float(input("Введите значение x1 -> "))
xn = float(input("Введите значение xn -> "))
delta_x = float(input("Введите значение Δx -> "))

# Инициализация списка для хранения результатов
results = []

# Вычисление значений функции в заданных точках с помощью цикла for
n_steps = int((xn - x1) / delta_x) + 1  # Количество шагов
for i in range(n_steps):
    x = x1 + i * delta_x
    if x > 0:  # Проверка, что x > 0
        y = b * math.log(a * x**2) + b * (math.log(x)**2)
        results.append((x, y))
    else:
        print(f"Пропускаем x = {x} из-за невалидного значения.")

# Вывод результатов
print("Результаты:")
for x, y in results:
    print(f"x = {x:.2f}, y = {y:.4f}")
