from math import *
import sys


x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))


# Выбор функции f(x)
msg = "Выберите вид функции f(x): 1 - sinh(y), 2 - x^e^x, 3 - sqrt(ln(x))"
choice = int(input(msg + "\n -> "))

# Вычисление f(x) в зависимости от выбора пользователя
if choice == 1:
    fx = sinh(y)
elif choice == 2:
    fx = x ** exp(x)
elif choice == 3:
    if x > 0:
        fx = sqrt(log(x))
    else:
        print("Ошибка: x должен быть больше 0 для функции ln(x)")
        sys.exit()
else:
    print("Неверный выбор функции!")
    sys.exit()

# Вычисление произведения x * y
xy = fabs(x * y)

# Определение a по условию
if xy > 10:
    a = log(fabs(fx) + fabs(y))
elif xy < 10:
    a = exp(fx + y)
elif xy == 10:
    a = pow(fx, 1/3) + y
else:
    print("Невозможно вычислить значение a")
    sys.exit()

# Вывод результата
print(f"Результат: a = {a}")
