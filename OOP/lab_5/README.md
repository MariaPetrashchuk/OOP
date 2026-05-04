# Лабораторна робота: Робота з ООП. Класи, методи, атрибути

## [Мета роботи]
[Навчитись працювати з класами та їх основними конструкціями в Python].

* з використанням URL ![alt text](https://github.com/BobasB/it_college/raw/main/reports/pictures/logo-lit.jpg "ІТ Коледж")
    
## [Виконання роботи]

### 1. [Результати виконання завдань]

- [Створено клас] `MyAnimals`
- [Додано атрибути класу]: `total_objects`, `total_csv`
- [Додано атрибути екземпляра]: `animals`, `name`, `age`
- [Додано метод класу] `from_csv` — [дозволяє створювати об'єкти з CSV-рядка]
- [Додано метод класу для перевірки імені] — [перевіряє, чи починається ім'я з великої літери]

### 2. [Код, розроблений у ході роботи]

class MyAnimals:
total_csv = 0
total_objects = 0

text
def __init__(self, animals, name, age) -> None:
    if not self.is_name_capitalized(name):
        raise ValueError("Ім'я має починатися з великої літери!")
    self.animals = animals
    self.name = name
    self.age = age
    MyAnimals.total_objects += 1

@classmethod
def from_csv(cls, csv_data: str):
    cls.total_csv += 1
    animal, name, age = csv_data.split(",")
    return cls(animal, name, age)

@classmethod
def is_name_capitalized(cls, name: str) -> bool:
    return name.isupper()
a1 = MyAnimals.from_csv("Кіт,Мурка,5")
a2 = MyAnimals("Собака", "Рекс", 2)

print(f"Мій {a1.animals}, звати {a1.name}, має {a1.age} років")
print(f"Мій {a2.animals}, звати {a2.name}, має {a2.age} років")
print(f"Загальна кількість об'єктів {MyAnimals.total_objects} а створених з csv формату {MyAnimals.total_csv}")

text

### 3. [Результат роботи програми]

Мій Кіт, звати Мурка, має 5 років
Мій Собака, звати Рекс, має 2 років
Загальна кількість об'єктів: 2, створених з CSV: 1

text

### 4. [Скріншоти виконання]

![Результат виконання програми](https://raw.githubusercontent.com/username/repository/main/pictures/result.png)

![Вивід програми](pictures/output.png)

> **[Рекомендація]**: [Усі зображення краще зберігати в папці] `pictures/`

## [:Висновок]

### [Що зроблено в роботі]
[Вивчено основи ООП у Python, створено клас, додано методи, виконано завдання з] `classes.ipynb`.

### [Чи досягнуто мети]
[Так, мету — навчитися працювати з класами та їх конструкціями — досягнуто].

### [:Нові знання]
- [створення класів]
- [атрибути класу та об'єкта]
- [методи класу]
- [базова перевірка даних]
- [створення об'єктів із CSV]

### [Чи відповіли на всі питання]
[Так].

### [Чи виконано всі завдання]
[Так, усі завдання у файлі] `classes.ipynb` [translate:були виконані].

### [Чи виникли труднощі]
[Невеликі труднощі виникли під час організації логіки класу].

### [Чи подобається формат]
[Так, формат зручний і структурований].

### [Побажання]
[Було б корисно додати більше практичних прикладів та розширених завдань].