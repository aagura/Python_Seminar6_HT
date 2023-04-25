# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод: Вывод:
# 1232 3 2
# 15 минут

n = int(input('Введите длину списка: '))
Spisok = [int(input(f'Введите {i + 1} элемент списка: ')) for i in range(n)]

def count_pairs (array):
    dict_numbers = {}
    count = 0
    for i in range(n):
        if array[i] in dict_numbers:
            dict_numbers[array[i]] += 1
        else:
            dict_numbers[array[i]] = 1
    for j,k in dict_numbers.items():
        if k > 1 : count = count + k//2
    return (count)

print (int (count_pairs (Spisok)))
