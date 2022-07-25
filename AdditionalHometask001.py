# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_row(path):
    with open(path, 'r') as polynom:
        y = polynom.read().replace(' - ', ' + -').split(' + ')
        print(y)
    return y


def get_list(data):
    poly = []
    for i in range(len(data)):
        try:
            if int(data[i]):
                data[i] += '*x^0'
        except:
            pass
        poly.append(list(data[i].split('x')))
        if poly[i][0] == '' and poly[i][1] != '':
            poly[i][0] = '1*'
        if poly[i][0] != '' and poly[i][1] == '':
            poly[i][1] = '^1'
        poly[i][1] = int(poly[i][1].replace('^', ''))
    return poly


def get_item(data):
    for i in range(len(data)):
        max_elem = data[0][1]
        if data[i][1] > max_elem:
            max_elem = data[i][1]
    item = [0]*max_elem
    for i in range(max_elem):
        try:
            item.insert(data[i][1], int(data[i][0].replace('*', '')))
            item.pop(data[i][1]+1)
        except:
            pass
    return item


def get_sum(item_1, item_2):
    res = list(map(lambda m, n: m+n, item_1, item_2))
    y = ''
    for i in range(len(res)):
        y = str(res[i])+'*x^'+str(i) + ' + ' + y
    y = y.replace('x^1 ', 'x ')
    y = y.replace('*x^0', '')
    y = y.replace(' 1*x', ' x')
    y = y.replace(' + -', ' - ')
    y = y[:-3]
    return y


path_1 = 'polynomial_1.txt'
path_2 = 'polynomial_2.txt'

print(get_sum(get_item(get_list(get_row(path_1))), get_item(get_list(get_row(path_2)))))
