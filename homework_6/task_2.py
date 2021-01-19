class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, specific_gravity, blade_thickness):
        return (self._length * self._width * specific_gravity * blade_thickness) / 1000


road_works_1 = Road(20, 5000)
print(f'Требуемая масса асфальта: {road_works_1.mass_calculation(25, 5)} т')
