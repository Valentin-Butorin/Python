class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is going.'

    def stop(self):
        return f'{self.name} is parked.'

    def turn(self, direction):
        dir_dict = {
            'left': f'{self.name} turned left.',
            'right': f'{self.name} turned right.'
        }
        return dir_dict[direction]

    def show_speed(self):
        return f'Current {self.name} speed: {self.speed} km/h.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Current {self.name} speed: {self.speed} km/h. Speed limit violation!'
        return f'Current {self.name} speed: {self.speed} km/h.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Current {self.name} speed: {self.speed} km/h. Speed limit violation!'
        return f'Current {self.name} speed: {self.speed} km/h.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lada = TownCar(75, 'black', 'Lada', False)
bmw = SportCar(120, 'red', 'BMW', False)
kamaz = WorkCar(35, 'orange', 'Kamaz', False)
chevrolet = PoliceCar(60, 'white', 'Chevrolet', True)

print(f'{lada.name}, {lada.color}, {lada.speed} km/h. Is {lada.name} a police car? {lada.is_police}')
print(f'{bmw.name}, {bmw.color}, {bmw.speed} km/h. Is {bmw.name} a police car? {bmw.is_police}')
print(f'{kamaz.name}, {kamaz.color}, {kamaz.speed} km/h. Is {kamaz.name} a police car? {kamaz.is_police}')
print(f'{chevrolet.name}, {chevrolet.color}, {chevrolet.speed} km/h. '
      f'Is {chevrolet.name} a police car? {chevrolet.is_police}')
print()
print(lada.go(), lada.show_speed())
print(lada.turn('left'))
print(lada.stop())
print()
print(bmw.go(), bmw.show_speed())
print(bmw.turn('right'))
print(bmw.stop())
print()
print(kamaz.go(), kamaz.show_speed())
print(kamaz.turn('right'))
print(kamaz.stop())
print()
print(chevrolet.go(), chevrolet.show_speed())
print(chevrolet.turn('left'))
print(chevrolet.stop())
