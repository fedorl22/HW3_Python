# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A i
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
try:
    n = int(input('Задайте количество элементов в массиве: '))
    lst = list()
    i = 0
    while i < n:
        lst.append(int(input(f'Введите {i} элемент массива')))
        i+=1
    x = int(input('Введите число X: '))

    count = 0
    for l in lst:
        
        if l == x:
            count+=1
            i+=1

    print(*lst)
    print(count)

except:
    print("Введены некоректные данные.")  