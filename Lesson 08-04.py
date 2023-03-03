

class Warehouse:
    def __init__(self, location):
        self.location = location
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
            else:
                print("Error: not enough items in stock.")
        else:
            print("Error: item not found in stock.")

    def list_items(self):
        print("Inventory of warehouse at location", self.location)
        for item, quantity in self.inventory.items():
            print(item.description(), quantity)


class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, print_type):
        super().__init__(brand, model, price)
        self.print_type = print_type

    # def __str__(self):
    #     return f"{self.brand} {self.model} ({self.print_type}) - ${self.price}"

    def description(self):
        return f"Printer: {self.brand} {self.model}, Print Type: {self.print_type}, Price: {self.price}"

class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, resolution):
        super().__init__(brand, model, price)
        self.resolution = resolution

    def description(self):
        return f"Scanner: {self.brand} {self.model}, Resolution: {self.resolution}, Price: {self.price}"

class Copier(OfficeEquipment):
    def __init__(self, brand, model, price, copy_speed):
        super().__init__(brand, model, price)
        self.copy_speed = copy_speed

    def description(self):
        return f"Copier: {self.brand} {self.model}, Copy speed: {self.copy_speed}, Price: {self.price}"

"""
Чтобы добавить товар на склад, необходимо создать объект класса Warehouse, 
а затем вызвать метод add_item() для этого объекта, передав в него 
объект товара и его количество. Например:
"""
# создаем объект склада
warehouse = Warehouse("Main Warehouse")

# создаем объект принтера
printer = Printer("HP", "OfficeJet Pro 9025", 249.99, "inkjet")

# добавляем 5 принтеров на склад
warehouse.add_item(printer, 5)

# добавляем товары на склад
printer1 = Printer("Canon", "PIXMA", 150, "inkjet")
warehouse.add_item(printer1, 10)

printer2 = Printer("Epson", "EcoTank", 250, "inkjet")
warehouse.add_item(printer2, 5)

scanner1 = Scanner("HP", "ScanJet", 100, "600x600")
warehouse.add_item(scanner1, 3)

# выводим информацию о количестве товара на складе
warehouse.list_items()

