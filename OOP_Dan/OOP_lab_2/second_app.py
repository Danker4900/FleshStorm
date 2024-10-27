# 1 Основні змінні різних типів даних

# Створення простих змінних
a = "змінна з текстом"     # str
b = 1                       # int
b1 = 1.1                    # float

# Створення списку (list)
c = ["a", 1, 1.25, "Слово", a]  # list містить різні типи даних
print("List c:", c)

# Створення словника (dict)
d = {"a": "Слово", "b": 1, a: b}  # dict із ключами та значеннями
print("Dictionary d:", d)

# Створення кортежу (tuple)
e = ("a", a)  # tuple, що є незмінним
print("Tuple e:", e)

# Створення множини (set)
f = {"ss", a}  # set, де значення мають бути унікальні
print("Set f:", f)

# Перевірка типів змінних
print("Тип змінної a:", type(a))
print("Тип змінної b:", type(b))
print("Тип змінної b1:", type(b1))
print("Тип змінної c:", type(c))
print("Тип змінної d:", type(d))
print("Тип змінної e:", type(e))
print("Тип змінної f:", type(f))


# 2 Виведення констант за допомогою звичайного виводу та форматованих рядків
print("Перша константа: ", True)
print(f"І можна так робити вивід? {False}")
print("Ще одна константа: ", None)

# 3 Використання вбудованих функцій і форматованих рядків

print(abs(-12.5), f"є рівним {abs(12.5)}")  # абсолютне значення
print(round(3.14159, 2), "це округлене значення числа Пі до двох знаків")
print(len("Привіт"), "є кількістю символів у слові 'Привіт'")


# 4 Приклад 1: Цикл for з range()
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")

# Приклад 2: Цикл for для ітерації по елементах списку
for letter in letters:
    print(f"Буква: {letter}")

# Приклад 3: Цикл while для зворотного відліку
countdown = 3
while countdown > 0:
    print(f"Зворотний відлік: {countdown}")
    countdown -= 1
print("Старт!")


# 5 Приклад 1: Проста умова з тернарним оператором
A = True
print("Значить А=True" if A else "Значить А=False")

# Приклад 2: Умовне розгалуження if-elif-else
age = 18
if age < 18:
    print("Вам ще не повноліття")
elif age == 18:
    print("Вам щойно виповнилося 18!")
else:
    print("Ви повнолітні")

# Приклад 3: Вкладені умови
number = -5
if number > 0:
    print("Це позитивне число")
else:
    if number == 0:
        print("Це нуль")
    else:
        print("Це негативне число")


# 6
A = 0
try:
    print("Що буде якщо", 10 / A, "?")  # Виникає помилка ділення на нуль
except ZeroDivisionError as e:
    print("Помилка:", e)  # Специфічне перехоплення ZeroDivisionError
finally:
    print("А ось воно що!")

# Інший приклад: обробка помилки типу даних
try:
    B = "5"
    print("Результат:", 10 + B)  # Виникає помилка типу даних
except TypeError as e:
    print("Помилка типу:", e)  # Специфічне перехоплення TypeError
finally:
    print("Спроба обробки завершена!")


# 7 Приклад 1: Читання файлу за допомогою контекст-менеджера
with open("README.md", "r") as f:
    for line in f:
        print(line.strip())  # Виводимо кожен рядок без зайвих переносів

# Приклад 2: Запис у файл за допомогою контекст-менеджера
with open("output.txt", "w") as f:
    f.write("Це новий рядок у файлі\n")
    f.write("І ще один рядок\n")

# Приклад 3: Контекст-менеджер з обробкою ресурсів (наприклад, для замірів часу)
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        print("Початок замірів часу...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Час виконання: {time.time() - self.start} секунд")


# 8 Використання контекст-менеджера для замірів часу
with Timer() as timer:
    total = sum(range(1000000))  # Деяка операція, яка займає час
    print("Сума чисел до мільйона:", total)

# Лямбда-функція для обчислення суми двох чисел
sum_lambda = lambda x, y: x + y
print("Це просто функція:", sum_lambda)
print("Це її виклик для обчислення 5 + 10:", sum_lambda(5, 10))

# Лямбда-функція для перевірки парності числа
is_even = lambda num: "Парне" if num % 2 == 0 else "Непарне"
print("Перевірка числа 4:", is_even(4))
print("Перевірка числа 7:", is_even(7))

# Лямбда-функція для використання в функції map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Квадрати чисел у списку:", squared_numbers)


# приклади ChatGPT

# 1. Змінні та типи даних
# Оголошення змінних
x = 10              # ціле число
y = 3.14            # число з плаваючою точкою
name = "ChatGPT"    # рядок

# Виведення типів даних
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(name))  # <class 'str'>

# 2. Умовні оператори
number = 10

if number > 0:
    print("Число додатнє")
elif number < 0:
    print("Число від’ємне")
else:
    print("Число дорівнює нулю")

# 3. Цикли
# Приклад циклу for
for i in range(5):
    print(i)  # Виводить числа від 0 до 4

# Приклад циклу while
count = 0
while count < 5:
    print(count)
    count += 1

# 4. Функції
def greet(name):
    return f"Привіт, {name}!"

print(greet("ChatGPT"))  # Виведе: Привіт, ChatGPT!

# 5. Робота зі списками
# Створення списку
fruits = ["яблуко", "банан", "вишня"]

# Додавання елемента
fruits.append("апельсин")

# Виведення елементів списку
for fruit in fruits:
    print(fruit)
