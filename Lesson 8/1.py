class Date:
    DAYS_IN_MONTHS = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, date_str):
        self.date = date_str
        self.date_dict = self.str_to_int(self.date)

    @classmethod
    def str_to_int(cls, date):
        if cls.verify(date):
            date_list = list(map(int, date.split('-')))
            return {'day': date_list[0], 'month': date_list[1], 'year': date_list[2]}

    @staticmethod
    def verify(date):
        date_list = list(map(int, date.split('-')))
        if date_list[1] in Date.DAYS_IN_MONTHS.keys():
            if date_list[2] % 4 == 0 and date_list[2] % 100 > 0 or date_list[2] % 400 == 0:
                last_day = Date.DAYS_IN_MONTHS[date_list[1]] + 1
            else:
                last_day = Date.DAYS_IN_MONTHS[date_list[1]]
            if 1 <= date_list[0] <= last_day:
                return True
            else:
                raise Exception('Incorrect day!')
        else:
            raise Exception('Incorrect month!')


date_1 = Date('12-11-2016')
print(date_1.date_dict)
print(Date.str_to_int('29-02-2020'))
