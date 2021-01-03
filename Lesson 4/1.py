from sys import argv


def payroll(hours, rate, bonus):
    return int(hours) * int(rate) + int(bonus)


script_name, working_hours, hourly_rate, bonus_sum = argv

print(payroll(working_hours, hourly_rate, bonus_sum))
