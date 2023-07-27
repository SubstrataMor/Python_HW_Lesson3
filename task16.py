# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

N = int(input('Введите число: '))
X = 3
A = []
for i in range(N):
    A.append(random.randint(0, 10))
print(A)
count = 0
for i in A:
    if A[i] == X:
        count += 1
print(f"X = {count}")

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# i = 0
# count = 0
# for _ in list_1:
#     if list_1[i] == k:
#         count += 1
#     i+=1
# print(count)

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count = 0
# for i in list_1:
#     if list_1[i] == k:
#         count += 1
# print(count)