# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

from random import randint as rnd


def fill_array(arr):
    for i in range(len(arr)):
        arr[i] = rnd(0, len(arr))
    print('Cписок всех элементов: ', '\n',  arr)


def order(arr):
    num = []
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            num.append(arr[i])
    print('Cписок неповторяющихся элементов: ', '\n',  num)


n = int(input('Введите размер последовательности: '))
numbers = ['']*n
fill_array(numbers)
print('Cписок однократно повторяющихся элементов: ', '\n', list(set(numbers)))
order(numbers)
