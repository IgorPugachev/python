class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} Машина поехала'

    def stop(self):
        return f'{self.name} Машина остановилась'

    def turn(self, direction):
        return f'{self.name} Машина повернула в направлении {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} составляет {self.speed}'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} превышает разрешенную для городского транспорта в данном зоне'
        else:
            return f'Скорость автомобиля {self.name} не превышает разрешенную'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше разрешенного лимита для рабочего автомобиля в данной зоне'
        else:
            return f'Скорость автомобиля {self.name} не превышает разрешенную'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'

    def sport(self):
        if self.is_police:
            return f'Автомобиль {self.name} является спортивным'
        else:
            return f'Автомобиль {self.name} не является спортивным'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'


Suzuki = TownCar(60, 'Black', 'Swift', True)
Toyota = WorkCar(40, 'White', 'Corolla', False)
Ford = SportCar(100, 'Green', 'Ute', True)
Mazda = PoliceCar(120, 'red',  'Infinity', True)

print(Toyota.turn("Направо"))
print(f'Когда {Suzuki.turn("Налево")}, то {Suzuki.stop()}')
print(f'{Ford.go()} со скоростью {Ford.show_speed()}')
print(f'{Mazda.name} цвета {Mazda.color}')

print(f'{Ford.name} полицейская машина? {Ford.is_police}')
print(f'{Toyota.name} полицейская машина? {Toyota.is_police}')

print(Mazda.show_speed())
print(Toyota.show_speed())
print(Ford.police())
print(Suzuki.show_speed())