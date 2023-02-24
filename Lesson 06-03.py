
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return "{} {}".format(self.name, self.surname)

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

worker = Position("Иван", "Петров", "инженер", 50000, 10000)
print("Полное имя сотрудника: {}".format(worker.get_full_name()))
print("Доход с учетом премии: {}".format(worker.get_total_income()))