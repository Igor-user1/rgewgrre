n = int(input('Ввести верхнюю грницу: '))
d = int(input('Ввести нижнюю границу: '))
p=0 #количество делителей числа в заданном диапазоне
m = 0 #количество делителей делителей числа в заданном диапазоне
prostoe_chislo = 0
for y in range(d, n + 1):
    if n % y == 0:
        for z in range(1,y+1):
            if y%z == 0:
                m1 = m+1
                m=m1
            if m==2:
                prostoe_chislo1= prostoe_chislo+1
                prostoe_chislo=prostoe_chislo1
        p = p+1
print(prostoe_chislo)contain