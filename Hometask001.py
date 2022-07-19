# # Вычислить число c заданной точностью d
# # Пример:
# # - при d = 3, π = 3.141

n = int(input('Введите число от 4000 до 40000: '))
d = int(input('Введите точность округления: '))
leibniz, madhava, basel, bbp = 0, 0, 0, 0
c = 0
for i in range(1, n):
    if i % 2 != 0:
        leibniz += (-1)**c*4/i
        madhava += (-1)**c*1/(i*3**c)
        c += 1
    basel += 1/i**2
    if i<257:
        bbp += (4/(8*(i-1)+1)-2/(8*(i-1)+4)-1/(8*(i-1)+5)-1/(8*(i-1)+6))/16**(i-1)
print(f'π = {round(leibniz, d)}')
print(f'π = {round(madhava*12**0.5, d)}')
print(f'π = {round((basel*6)**0.5, d)}')
print(f'π = {round(bbp, d)}')
