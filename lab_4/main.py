class MyName:
    """Клас для роботи з іменами користувачів"""
    
    total_names = 0

    def __init__(self, name=None) -> None:
        """Ініціалізація класу"""
        if name is None:
            self.name = "Anonymous"
        else:
            self.name = name.capitalize()
        
        if not self.name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        
        MyName.total_names += 1
        self.my_id = MyName.total_names
        self._email_domain = "itcollege.lviv.ua"

    @property
    def whoami(self) -> str: 
        """Class property - повертає представлення"""
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property - повертає email"""
        return self.create_email()
    
    @property
    def full_name(self) -> str:
        """Повна інформація про користувача"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    
    def create_email(self) -> str:
        """Instance method - створює email"""
        return f"{self.name.lower()}@{self._email_domain}"
    
    def change_email_domain(self, new_domain: str) -> None:
        """Змінює домен email"""
        if '@' in new_domain or not new_domain.replace('.', '').isalpha():
            raise ValueError("Некоректний домен")
        self._email_domain = new_domain
    
    def count_name_letters(self) -> int:
        """Підраховує кількість букв у імені"""
        return len(self.name)
    
    def save_to_file(self, filename: str = "users.txt") -> None:
        """Зберігає інформацію у файл"""
        with open(filename, "a", encoding='utf-8') as f:
            f.write(self.full_name + "\n")

    @classmethod
    def anonymous_user(cls):
        """Class method - створює анонімного користувача"""
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message: str = "Hello to everyone!") -> str:
        """Static method - привітання"""
        return f"You say: {message}"


# Використання
print("Розпочинаємо створювати об'єкти!")

names = ("Марія", "Олександр", None, "Іван", "Анна")
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

print(f"\nWe are done. We create {MyName.total_names} names!")

# Додаткові демонстрації
print("\n" + "="*70)
print("ДОДАТКОВІ ПРИКЛАДИ:")
print("="*70)

# Підрахунок букв
print("\n1. Підрахунок букв:")
for name, me in all_names.items():
    print(f"{me.name}: {me.count_name_letters()} букв")

# Властивість full_name
print("\n2. Повна інформація:")
for name, me in all_names.items():
    print(me.full_name)

# Зміна email домену
print("\n3. Зміна email домену:")
maria = all_names["Марія"]
print(f"До зміни: {maria.my_email}")
maria.change_email_domain("gmail.com")
print(f"Після зміни: {maria.create_email()}")

# Різні привітання
print("\n4. Привітання:")
print(MyName.say_hello())
print(MyName.say_hello("Привіт, Україно!"))

# Збереження у файл
print("\n5. Збереження у файл:")
filename = "users.txt"
with open(filename, "w", encoding='utf-8') as f:
    f.write("")
for name, me in all_names.items():
    me.save_to_file(filename)
print(f"Збережено у {filename}")

# Перевірка валідації
print("\n6. Перевірка валідації:")
try:
    invalid = MyName("John123")
except ValueError as e:
    print(f"Помилка: {e}")

# Автоматичне перетворення
print("\n7. Автоматичне перетворення:")
test = MyName("марія")
print(f"'марія' → '{test.name}'")
