
# создаем класс Road с конструктором, который принимает два параметра - длину и ширину дороги,
# и сохраняет их в защищенных атрибутах _length и _width.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_asphalt_mass(self, asphalt_mass_per_sq_meter, thickness_cm):
        asphalt_mass_in_kg = (asphalt_mass_per_sq_meter * thickness_cm * self._length * self._width) / 1000
        print(f'Потребуется {asphalt_mass_in_kg} кг асфальта')

# сначала создаем экземпляр класса, в который передаем значения атрибутов length и width
my_road = Road(20, 5000)
# а потом для этого экземпляра класса вызываем метод класса, считающий расход асфальта.
my_road.calculate_asphalt_mass(25, 5)
