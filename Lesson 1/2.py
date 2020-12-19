time = int(input('Пожалуйста, введите время в секундах: '))
hh = str(time // 60 // 60 // 10) + str(time // 60 // 60 % 10)
mm = str(time // 60 % 60 // 10) + str(time // 60 % 60 % 10)
ss = str(time % 60 // 10) + str(time % 60 % 10)

print(f'{hh}:{mm}:{ss}')