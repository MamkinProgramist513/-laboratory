import math

# Ввод значений a, b, x1, xn и Δx
a = float(input("Введите значение a -> "))
b = float(input("Введите значение b -> "))
x1 = float(input("Введите значение x1 -> "))
xn = float(input("Введите значение xn -> "))
delta_x = float(input("Введите значение Δx -> "))

# Инициализация списка для хранения результатов
results = []
x = x1  # Начальное значение x

# Вычисление значений функции в заданных точках с помощью цикла while
while x <= xn:
    if x > 0:  # Проверка, что x > 0
        y = b * math.log(a * x**2) + b * (math.log(x)**2)
        results.append((x, y))
    else:
        print(f"Пропускаем x = {x} из-за невалидного значения.")
    x += delta_x  # Переход к следующему значению x

# Вывод результатов
print("Результаты:")
for x, y in results:
    print(f"x = {x:.2f}, y = {y:.4f}")
1.4