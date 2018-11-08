#!/usr/bin/env python3
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
exempl = '''
Protocol:           OSPF
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}
'''

with open('ospf.txt', 'r') as f:
	for line in f:
		lst = line.replace(',','').split()
		print(exempl.format(lst[1], lst[2], lst[4], lst[5], lst[6]))
