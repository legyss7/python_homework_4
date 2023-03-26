# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в 
# обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы 
# множеств.

import random
import module_quicksort as sort

length_n = int(input("Введите количество элементов первого множества: "))
length_m = int(input("Введите количество элементов второго множества: "))

numbers_n = {random.randint(1, length_n) for _ in range(length_n)}
numbers_m = {random.randint(1, length_m) for _ in range(length_m)}

print(numbers_n)
print(numbers_m)

numbers_i = list(numbers_n.intersection(numbers_m))
# print(numbers_i)

print(sort.quicksort(numbers_i))
