#!/usr/bin/env python3
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config):
	'''
	Функция ожидает txt файл.
	На выходе получаем два словаря: для access и trunk портов.
	Дополнение: конфигурация access портов в авторежиме.
	'''
	access_dict = {}
	trunk_dict = {}
	with open(config) as file_in:
		for line in file_in:
			if 'interface' in line:
				key = line.split()[-1]
			if 'mode access' in line:
				access_dict[key] = 1
			if 'access vlan' in line:
				access_dict[key] = line.split()[-1]
			if 'allowed vlan' in line:
				vlans = line.split()[-1]
				trunk_dict[key] = [int(vlan) for vlan in vlans.split(',')]
	print(access_dict, '\n', trunk_dict)
	
get_int_vlan_map('config_sw2.txt')
