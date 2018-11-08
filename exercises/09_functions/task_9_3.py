#!/usr/bin/env python3
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config):
	'''
	Функция ожидает txt файл.
	На выходе получаем два словаря: для access и trunk портов.
	'''
	access_dict = {}
	trunk_dict = {}
	with open(config) as file_in:
		for line in file_in:
			if 'interface' in line:
				key = line.split()[-1]
			if 'access vlan' in line:
				access_dict[key] = line.split()[-1]
			if 'allowed vlan' in line:
				vlans = line.split()[-1]
				trunk_dict[key] = [int(vlan) for vlan in vlans.split(',')]
	print(access_dict, '\n', trunk_dict)
	
get_int_vlan_map('config_sw1.txt')
