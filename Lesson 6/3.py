class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return sum(self._income.values())


salesman1 = Position('Ivan', 'Ivanov', 'salesman', 35000, 5000)
salesman2 = Position('Michael', 'Jackson', 'salesman', 30000, 2500)
supervisor1 = Position('Lucifer', 'Morningstar', 'supervisor', 421, 245)
supervisor2 = Position('Nameless', 'Anonymous', 'supervisor', 11, 6)

print(f'{salesman1.get_full_name()} is {salesman1.position}, his total income is {salesman1.get_total_income()}')
print(f'{salesman2.get_full_name()} is {salesman2.position}, his total income is {salesman2.get_total_income()}')
print(f'{supervisor1.get_full_name()} is {supervisor1.position}, his total income is {supervisor1.get_total_income()}')
print(f'{supervisor2.get_full_name()} is {supervisor2.position}, his total income is {supervisor2.get_total_income()}')
