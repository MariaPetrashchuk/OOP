from abc import ABC, abstractmethod
from random import randint, choice

# ================== АБСТРАКЦІЯ ==================
class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another_item):
        pass


# ================== SWORD ==================
class Sword(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0
        self._boost = 0

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10) + self._boost
        self._boost = 0
        another_item.health -= current_attack
        return f"⚔️ {self.name} наносить {current_attack} шкоди!"

    def sharpening(self):
        self._sharp += 1
        return "Меч загострено (+1 sharp)"

    def boost(self):
        self._boost = 10
        return "⚡ Меч отримав тимчасове підсилення (+10 до наступної атаки)"


# ================== AXE ==================
class Axe(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._boost = 0

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(0, 20) + self._boost
        self._boost = 0
        another_item.health -= current_attack
        return f"🪓 {self.name} наносить {current_attack} шкоди!"

    def boost(self):
        self._boost = 15
        return "🔥 Сокира отримала підсилення (+15 до наступної атаки)"


# ================== BOW ==================
class Bow(Item):
    def __init__(self, name, attack_power: int, range_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._range_power = range_power
        self._boost = 0

    def attack(self, another_item: Item):
        current_attack = (
            self.__attack_power
            + randint(5, 15)
            + self._range_power
            + self._boost
        )
        self._boost = 0
        another_item.health -= current_attack
        return f"🏹 {self.name} випускає стрілу та наносить {current_attack} шкоди!"

    def reload(self):
        self._range_power += 1
        return "🎯 Дальність лука збільшена (+1 range)"

    def boost(self):
        self._boost = 12
        return "✨ Лук заряджено магією (+12 до наступної атаки)"


# ================== ВИПАДКОВИЙ ВИБІР ЗБРОЇ ==================
weapons = [
    Sword("Ескалібур", 100),
    Axe("Кратос", 95),
    Bow("Ельфійський лук", 85, 5)
]

player = choice(weapons)
enemy = choice([w for w in weapons if w != player])

print(f"\n🎮 Ви граєте за: {player.name}")
print(f"👾 Проти вас: {enemy.name}\n")


# ================== ПОКРОКОВА ГРА ==================
turn = 1

while player.health > 0 and enemy.health > 0:
    print(f"\n--- Хід {turn} ---")
    print(f"Ваше здоров'я: {player.health}")
    print(f"Здоров'я ворога: {enemy.health}")

    print("\nОберіть дію:")
    print("1 - Атакувати")
    print("2 - Підсилення")

    choice_input = input("Ваш вибір: ")

    if choice_input == "1":
        print(player.attack(enemy))
    elif choice_input == "2":
        if isinstance(player, Sword):
            print(player.sharpening())
        elif isinstance(player, Bow):
            print(player.reload())
        else:
            print(player.boost())
    else:
        print("Невірний вибір!")

    if enemy.health <= 0:
        print(f"\n🏆 Перемога за вами! ({player.name})")
        break

    # Хід ворога (проста логіка)
    if randint(0, 1) == 0:
        print(enemy.attack(player))
    else:
        if hasattr(enemy, "boost"):
            print(enemy.boost())

    if player.health <= 0:
        print(f"\n💀 Ви програли! Переміг {enemy.name}")
        break

    turn += 1
