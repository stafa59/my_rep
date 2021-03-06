#!/usr/bin/env python3
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

src = input('Введите исходный файл:\n')
out = input('Введите итоговый файл:\n')

with open(src, 'r') as f1, open(out, 'w') as f2:
	for line in f1:
		for elem in ignore:
			if line.count(elem) != 0:
				break
			elif elem == ignore[len(ignore)-1]:
				f2.write(line)
