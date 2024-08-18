first = int(input('Введите первое число: '))

second = int(input('Введите второе число: '))

third = int(input('Введите третье число: '))


if first == second:
    if second == third:
        print(3)
    else:
        print(2)
elif first == third:
    print(2)
elif second == third:
    print(2)
else:
    print(0)
