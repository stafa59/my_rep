#!/usr/bin/env python3
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


with open('config_sw1.txt', 'r') as f1, open('config_sw1_cleared.txt', 'w') as f2:
	for line in f1:
		for elem in ignore:
			if line.count(elem) != 0:
				break
			elif elem == ignore[len(ignore)-1]:
				f2.write(line)
