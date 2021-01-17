class Road:
    def __init__(self, length, width):
        self._length_m = length
        self._width_m = width

    def calc_weight(self, sq_m_weight_kg, depth_cm):
        return self._length_m * self._width_m * sq_m_weight_kg * depth_cm // 1000


irkutsk_moscow = Road(5000, 20)
print(irkutsk_moscow.calc_weight(25, 5))
