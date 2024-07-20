fist = input('Введите первое число:  ')
second = input('Введите второе число:  ')
third = input('Введите третье число:  ')

if fist == second == third:
    print(3)
elif fist == second or second == third or third == fist:
    print(2)
else:
    print(0)