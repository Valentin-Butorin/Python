class Storage:
    id = 1

    def __init__(self, name):
        self.name = name
        self.database = {
            'Printer': [],
            'Scanner': [],
            'Copier': []
        }

    def __str__(self):
        return self.name

    def inventory(self, quantity: int, class_obj):
        if self.database[class_obj.device_type]:
            for i, item in enumerate(self.database[class_obj.device_type], 0):
                if class_obj in item:
                    self.database[class_obj.device_type][i][1] += quantity
                    break
            else:
                self.database[class_obj.device_type].append([class_obj, quantity])
        else:
            self.database[class_obj.device_type].append([class_obj, quantity])
        print(f'{quantity} шт. "{class_obj}" - поступление в место хранения "{self.name}"')

    def transfer(self, consignee, quantity: int, class_obj):
        for i, item in enumerate(self.database[class_obj.device_type], 0):
            if class_obj in item:
                try:
                    if self.validate_quantity(class_obj, quantity):
                        self.database[class_obj.device_type][i][1] -= quantity
                        print(f'{quantity} шт. "{class_obj}" - отгрузка из места хранения "{self}".')
                        return consignee.inventory(quantity, class_obj)
                except QuantityError as err:
                    print(err)
            break

    def validate_quantity(self, class_obj, quantity):
        for i, item in enumerate(self.database[class_obj.device_type], 0):
            if class_obj in item:
                if quantity <= self.database[class_obj.device_type][i][1]:
                    return True
                else:
                    raise QuantityError(self, class_obj, quantity)

    @property
    def total_remains(self):
        total = 0
        for items in self.database.values():
            for item in items:
                total += item[1]
        return f'Всего устройств в месте хранения "{self.name}" - {total}'

    @property
    def report_remains(self):
        return self.printing_form_remains(self.name, self.database, self.total_remains)

    @staticmethod
    def printing_form_remains(name, db, total):
        output = f'Отчет по остаткам ({name}):\n'
        for group in db.keys():
            output += f'- {group} -\n'
            for item in db[group]:
                output += f'{item[0]} - {item[1]}\n'
        output += total
        return output


class OfficeEquipment:
    def __init__(self, brand, model):
        self.device_type = self.__class__.__name__
        self.brand = brand
        self.model = model
        self.id = Storage.id
        Storage.id += 1


class Printer(OfficeEquipment):
    def __init__(self, brand, model, technology, color, interface):
        super().__init__(brand, model)
        self.technology = technology
        self.color = color
        self.interface = interface

    def __str__(self):
        return f'{self.device_type} {self.brand} {self.model} {self.technology} ' \
               f'{self.interface} {self.color} (артикул: {self.id})'

    def __repr__(self):
        return f'{self.device_type} {self.brand} {self.model} {self.technology} ' \
               f'{self.interface} {self.color} (артикул: {self.id})'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, color, interface):
        super().__init__(brand, model)
        self.device_type = self.__class__.__name__
        self.color = color
        self.interface = interface

    def __str__(self):
        return f'{self.device_type} {self.brand} {self.model} {self.interface} ' \
               f'{self.color} (артикул: {self.id})'

    def __repr__(self):
        return f'{self.device_type} {self.brand} {self.model} {self.interface} ' \
               f'{self.color} (артикул: {self.id})'


class Copier(OfficeEquipment):
    def __init__(self, brand, model, technology, color, interface):
        super().__init__(brand, model)
        self.device_type = self.__class__.__name__
        self.technology = technology
        self.color = color
        self.interface = interface

    def __str__(self):
        return f'{self.device_type} {self.brand} {self.model} {self.technology} ' \
               f'{self.interface} {self.color} (артикул: {self.id})'

    def __repr__(self):
        return f'{self.device_type} {self.brand} {self.model} {self.technology} ' \
               f'{self.interface} {self.color} (артикул: {self.id})'


class QuantityError(Exception):
    def __init__(self, storage, item, quantity):
        self.text = f'Ошибка! {item} {quantity} шт. - отгружаемое количество ' \
                    f'отсутствует в месте хранения "{storage}"'

    def __str__(self):
        return self.text


warehouse = Storage('Склад')
office = Storage('Офис')
directors_office = Storage('Кабинет директора')
store = Storage('Торговый зал')

kyocera = Printer('Kyocera', 'mf-450', 'Jet', 'white', 'USB')
brother = Printer('Brother', 'dcp-1510', 'Laser', 'gray', 'USB/LAN/WiFi')
sony = Scanner('Sony', 'kx-410', 'black', 'USB')
hp = Scanner('HP', 'S-441', 'white', 'USB')
xerox = Copier('Xerox', 'xn-220', 'Laser', 'gray', 'USB/LAN')
epson = Copier('Epson', 'e-1610', 'Jet', 'gray', 'USB/LAN/WiFi')

warehouse.inventory(2, kyocera)
warehouse.inventory(3, brother)
warehouse.inventory(5, brother)
warehouse.inventory(7, sony)
warehouse.inventory(1, hp)
warehouse.inventory(3, xerox)
warehouse.inventory(4, epson)

print(warehouse.report_remains)

warehouse.transfer(office, 1, kyocera)
warehouse.transfer(directors_office, 7, sony)
warehouse.transfer(store, 5, epson)

print(warehouse.report_remains)
print(office.report_remains)
print(directors_office.report_remains)
print(store.report_remains)
