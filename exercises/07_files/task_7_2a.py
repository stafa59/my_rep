#!/usr/bin/env python3
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt', 'r') as f:
	for line in f:
		if line[0] != '!':
			for elem in ignore:
				if line.count(elem) != 0:
					break
				elif elem == ignore[len(ignore)-1]:
					print(line.rstrip())
