class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5
    def mass_asph(self):
        mass_asph = self._width * self._length * self.weight * self.height
        print(f"Масса асфальта = {mass_asph/1000} т")

class Road1(Road):
    def mass_asph1(self):
        print(f"Масса асфальта = {20*5000*25*5/1000} т")

a = Road1(5000, 20)
a.mass_asph1()
a.mass_asph()