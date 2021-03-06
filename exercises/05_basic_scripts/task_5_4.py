#!/usr/bin/env python3
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4; в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

#N1 = 9
#N2 = 7


print('Введите элемент (', str(set(num_list)).strip('{}'), '): ')
el1 = int(input())
print('Введите элемент (', str(set(word_list)).strip('{}'), '): ')
el2 = str(input())

num_list.reverse()
word_list.reverse()

index1 = 9 - num_list.index(el1)
index2 = 7 - word_list.index(el2)
print(index1, ' / ', index2)
