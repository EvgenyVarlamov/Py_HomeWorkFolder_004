# Задайте натуральное число N. Напишите программу, которая составит
# список простых делителей числа N. (1 - составное число)

def simple(x):
    c = 0
    for i in range(2, x):
        if x % i == 0:
            c += 1
    if c > 0:
        return ''
    else:
        return x


def sim_row(x):
    arr = []
    for i in range(2, x+1):
        if simple(i):
            arr.append(i)
    return arr


def divisors(arr, x):
    div = []
    for i in range(len(arr)):
        if x % arr[i] == 0:
            div.append(arr[i])
    return div


n = int(input('Введите число: '))
list = []
list = (sim_row(n))
print(f'Список простых делителей числа {n}: {divisors(list,n)}')
