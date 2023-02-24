from abc import ABC, abstractmethod

# Определяем три класса: Clothes (абстрактный базовый класс для одежды),
# Coat (класс для пальто) и Suit (класс для костюма). Класс Clothes
# определяет основную структуру объектов одежды и содержит
# абстрактный метод fabric_consumption, который должен быть
# реализован в наследниках и возвращать расход ткани для данного типа одежды.
class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass

# Классы Coat и Suit определяют конкретные типы одежды и реализуют
# метод fabric_consumption в соответствии с заданными формулами.
class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 2)


coat = Coat('My coat', 52)
suit = Suit('My suit', 180)
print(coat.fabric_consumption)  # 8.54
print(suit.fabric_consumption)  # 360.3

# Для подсчета суммарного расхода ткани по всем видам одежды создаем класс Wardrobe,
# который содержит список всех добавленных в него предметов одежды.

class Wardrobe:
    def __init__(self):
        self.items = []
# Метод add_item позволяет добавлять новые элементы в гардероб
    def add_item(self, item):
        self.items.append(item)

# метод total_fabric_consumption возвращает суммарный расход ткани по всем элементам гардероба.
    @property
    def total_fabric_consumption(self):
        return round(sum([item.fabric_consumption for item in self.items]), 2)

# Создаем экземпляр класса Wardrobe
wardrobe = Wardrobe()
# Используя метод add_item, добавляем в него данные по пальто
wardrobe.add_item(coat)
# Используя метод add_item, добавляем в него данные по костюму
wardrobe.add_item(suit)
# Выводим общий расход ткани
print(wardrobe.total_fabric_consumption)  # 368.84
