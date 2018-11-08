#!/usr/bin/env python3
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
from tabulate import tabulate
from task_12_2 import check_ip_availability

def ip_table(reachable, unreachable):
	'''
	Представляет два списка в виде таблицы
	'''
	ip_lists = []
	for i in range(0, len(unreachable)):
		ip_lists.append([reachable[i], unreachable[i]])

	return tabulate(ip_lists, headers = ['Reachable', 'Unreachable'])

ip_list = '192.168.1.1-3'
reachable, unreachable = check_ip_availability(ip_list)
if len(reachable) > len(unreachable):
	while len(reachable) > len(unreachable):
		unreachable.append(' ')
else:
	while len(reachable) < len(unreachable):
		while len(reachable) < len(unreachable):
			reachable.append(' ')
print(reachable, unreachable)
print(ip_table(reachable, unreachable))
