# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input('Введите длину списка: '))
Spisok = [int(input(f'Введите {i + 1} элемент списка: ')) for i in range(n)]
min = int(input ('Введите нижнюю границу диапазона:'))
max = int(input ('Введите верхнюю границу диапазона: '))
if max < min : max,min = min,max
Spisok_range = []
for i in range (n):
    if Spisok [i]>= min and Spisok [i]<= max:

        Spisok_range.append(i)
print (Spisok_range)

