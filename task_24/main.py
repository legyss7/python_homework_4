# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на 
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у 
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве 
# внедрена система автоматического сбора черники. Эта система состоит из управляющего 
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь 
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух 
# соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во 
# входном файле грядки.

import random

number_of_bushes = int(input('Введите количество кустов: '))
number_of_berries = [random.randint(10, 50) for _ in range(number_of_bushes)]

print(f'Количество ягод на каждом кусте: {number_of_berries}')

number_of_berries_count = list()
for i in range(len(number_of_berries)-1):
    number_of_berries_count.append(
        number_of_berries[i-1] + number_of_berries[i] + number_of_berries[i+1])
number_of_berries_count.append(
    number_of_berries[-2] + number_of_berries[-1] + number_of_berries[0])
# print(number_of_berries_count) 
print(f'Максимальное количество ягод: {max(number_of_berries_count)}')