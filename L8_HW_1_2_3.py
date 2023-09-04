# 

# Задание №1

v = int(input('Введите количество элементов списка: '))
mass = []

for i in range(0, v):
    n = int(input('Введите любое целое число от 1 до 10001: '))
    while 1 > n or n > 10000:
        n = int(input("""Вы ввели число вне диапазона от 1 до 10001 !!!
Введите число еще раз: """))
    else:
        mass.append(n)

mass.reverse()
print(mass)


# Задание №2

n = int(input('Введите количество элементов списка от 1 до 100001: '))
while n < 1 or n > 100000:
    n = int(input("""Внимание!!! Количество элементов списка должно быть 
в диапазоне от 1 до 100001.
Попробуйте еще раз: """))
if n == 1:
    k = "число"
elif n == 2 or n == 3 or n == 4:
    k = "числа"
else:
    k = "чисел"

ind = 0  
lst = list(map(int, input(f"Введите {n} {k} через пробел, в диапазоне от 1 до 1000000001: ").split()))
while len(lst) != n:
    lst = list(map(int, input(f"Не верное количество элементов! Введите {n} {k} через пробел, в диапазоне от 1 до 1000000001: ").split()))
for x in lst:
    if x < 1 or x > 1000000000:
        lst[ind] = int(input(f"Замените значение элемента списка с {x} на допустимое значение в диапазоне от 1 до 1000000001: "))
        ind += 1
    else:
        ind += 1

mass = lst
mass.insert(0, lst[-1])
mass.pop(-1)
print (mass)


#

m = int(input("Введите грузоподъёмность одной лодки в диапазоне от 1 до 1.000.001: ")) 
while m < 1 or m > 1_000_000:
    m = int(input("Введите правильный диапазон грузоподъёмности одной лодки от 1 до 101: "))
print (m)
n = int(input("Введите количество рыбаков от 1 до 101: "))
while n < 1 or n > 100:
    n = int(input("Введите количество рыбаков от 1 до 101: "))
print (n)
eomass = []
for count in range(0, n):
    ai = int (input(f"Введите вес {count + 1}-го рыбака из {n}, вес которого от 1 до {m}: "))
    while ai < 1 or ai > m:
	    ai = int (input(f"Не тот вес у рыбака! Введите внимательно вес рыбака, от 1 до {m}: "))
    else:
        eomass.append(ai)

eomass.sort()
x = len(eomass)
boat = 0
while x > 0:
    if len(eomass) == 1:
        eomass.pop(0)
        x -=1
        boat +=1
    elif len(eomass) == 2 and (eomass[0] + eomass[1]) <= m:
        eomass.pop(0)
        eomass.pop(-1)
        x -= 2
        boat +=1
    elif len(eomass) == 2 and (eomass[0] + eomass[1]) > m:
        eomass.pop(-1)
        x -= 1
        boat += 1
    elif len(eomass) >= 3 and (eomass[0] + eomass[1]) <= m:
        eomass.pop(0)
        eomass.pop(-1)
        x -= 2
        boat +=1
    else:
        eomass.pop(-1)
        x -= 1
        boat +=1

print (boat)