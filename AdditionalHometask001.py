# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

y = ''
data = open('polynomial_1.txt', 'r')
y = data.readline()
data = open('polynomial_2.txt', 'r')
y += ' + ' + data.readline()
data
data.close()
print(y)
