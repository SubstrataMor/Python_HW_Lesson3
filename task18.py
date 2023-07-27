# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу k. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число k
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

N = int(input('Введите число: '))
k = 2
list_1 = []
for i in range(N):
    list_1.append(random.randint(0, 10))
list_1.sort()
print(list_1)
for i in range(len(list_1) - 1):
    if list_1[i] == k:
        print(list_1[i])
        break
    elif list_1[i] < k & k < list_1[i+1]:
        average = (list_1[i]+list_1[i+1])/2
        if k < average:
            print(list_1[i])
            break
        elif k == average:
            print(list_1[i], list_1[i+1])
            break
        else:
            print(list_1[i+1])
            break
    elif k > max(list_1):
        print(max(list_1))
        break
    elif k < min(list_1):
        print(min(list_1))
        break