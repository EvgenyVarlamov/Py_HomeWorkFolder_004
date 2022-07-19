# # Вычислить число c заданной точностью d
# # Пример:
# # - при d = 3, π = 3.141

n = int(input('Введите число от 4000: '))
d = int(input('Введите точность округления: '))
leibniz, madhava, basel = 0, 0, 0
c = 0
for i in range(1, n):
    if i % 2 != 0:
        leibniz += (-1)**c*4/i
        madhava += (-1)**c*1/(i*3**c)
        c += 1
    basel += 1/i**2
print(f'π = {round(leibniz, d)}')
print(f'π = {round(madhava*12**0.5, d)}')
print(f'π = {round((basel*6)**0.5, d)}')
