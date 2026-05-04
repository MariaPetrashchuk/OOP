a = "змінна з текстом"
b = 1              
b1 = 1.1           

c = ["a", 1, 1.25, "Слово", a]      
d = {"a": "Слово", "b": 1, a: b}     
e = ("a", a)                    
f = {"ss", a + " " + str(b)}       

print("a =", a, "| тип:", type(a))
print("b =", b, "| тип:", type(b))
print("b1 =", b1, "| тип:", type(b1))
print("c =", c, "| тип:", type(c))
print("d =", d, "| тип:", type(d))
print("e =", e, "| тип:", type(e))
print("f =", f, "| тип:", type(f))

print("\nДоступ до елементів:")
print("c[0] =", c[0])
print("d['a'] =", d["a"])
print("e[1] =", e[1])

print("Перша константа:", True)
print("Друга константа:", False)
print(f"Третя константа (через форматований рядок): {None}")

print(f"Булеве значення True дорівнює {int(True)} у числовому вигляді")
print(f"Булеве значення False дорівнює {int(False)} у числовому вигляді")

import sys

print("\n=== Зарезервовані слова Python ===")
help("keywords")


print(abs(-12.5), f"є рівним {abs(12.5)}", "і якщо порівняти то:", abs(-12.5) == abs(12.5))

text = "Привіт, Python!"
print("\nДовжина тексту:", len(text), "символів")

num = 3.1415926
print("\nОригінальне число:", num)
print("Округлене до 2 знаків:", round(num, 2))
print("Округлене до цілого:", round(num))


print("=== Приклад 1: цикл for з range() ===")
for i in range(5):
    print(f"Ітерація №{i}")
print("Цикл for завершено!\n")

print("=== Приклад 2: цикл for для списку ===")
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Цей цикл завершився без переривання!\n")


print("=== Приклад 3: цикл while ===")
count = 0
while count < 3:
    print(f"Лічильник: {count}")
    count += 1
else:
    print("Цикл while завершився, умова більше не виконується!\n")


print("=== Приклад 4: цикл for з break ===")
for num in range(10):
    if num == 5:
        print("Досягли числа 5 — перериваємо цикл!")
        break
    print("num =", num)
else:
    print("Цей текст не буде виконано, бо цикл завершився через break.")


from random import randint

A = randint(0, 1)
if A == 1:
    print(f"Значить A = {A}, отже умова істинна.")
else:
    print(f"Але може бути, що A = {A}, тому умова хибна.")


print("\n=== Приклад 2: if-elif-else ===")
B = randint(-10, 10)
if B > 0:
    print(f"Число B = {B} — додатне.")
elif B == 0:
    print(f"Число B = {B} — це нуль.")
else:
    print(f"Число B = {B} — від’ємне.")

print("\n=== Приклад 3: тернарний оператор ===")
C = randint(1, 100)
print(f"Число {C} є парним." if C % 2 == 0 else f"Число {C} є непарним.")

print("=== Приклад : Ділення на нуль ===")
A = 0
try:
    print("Що буде, якщо поділити 10 на", A, "? ->", 10 / A)
except Exception as e:
    print("Невже це помилка >", e)
finally:
    print("Цей блок виконується завжди, навіть якщо була помилка!\n")

with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Перший рядок\n")
    f.write("Другий рядок\n")
    f.write("Третій рядок\n")

print("Файл 'example.txt' створено і в нього записано кілька рядків.\n")

with open("example.txt", "r", encoding="utf-8") as f:
    print("=== Вміст файлу ===")
    for i, line in enumerate(f, start=1):
        print(f"{i})> {line.strip()}") 

print("\nФайл автоматично закрито після виходу з блоку 'with'.")

from contextlib import suppress

print("\n=== Приклад 3: контекст-менеджер suppress() ===")

with suppress(FileNotFoundError):
    with open("non_existing_file.txt", "r") as f:
        print(f.read())

print("Помилки FileNotFoundError не було виведено — вона була пригнічена.")

def add(a, b):
    return a + b

print("Звичайна функція add(2, 3):", add(2, 3))

add_lambda = lambda a, b: a + b
print("Те саме через лямбда:", add_lambda(2, 3))

introduce = lambda name, age: f"Мене звати {name}, мені {age} років"
print(introduce("Іван", 25))

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("\nКвадрати чисел за допомогою map() + lambda:", squares)


people = [("Олег", 25), ("Анна", 19), ("Богдан", 30)]
sorted_people = sorted(people, key=lambda x: x[1])
print("\nВідсортовані за віком:", sorted_people)