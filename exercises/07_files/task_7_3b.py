#!/usr/bin/env python3
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

set1 = set()
list1 = []

with open('CAM_table.txt', 'r') as f1:
	for line in f1:
		if line.count('.') == 2:
			list1.append(line.replace('    DYNAMIC ', ''))
			set1.add(line.replace('    DYNAMIC ', '').split()[0])

vlans = list(set1)
vlans.sort()
vlan = input('Введите номер vlan: ')	

for line in list1:
	if vlan == line.split()[0]:
		print(line.rstrip())
