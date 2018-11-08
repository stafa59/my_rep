#!/usr/bin/env python3
'''
Задание 9.2a

Сделать копию скрипта задания 9.2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


def generate_trunk_config(trunk):
	'''
	trunk - словарь trunk-портов,
	для которых необходимо сгенерировать конфигурацию, вида:
		{ 'FastEthernet0/1':[10,20],
		  'FastEthernet0/2':[11,30],
		  'FastEthernet0/4':[17] }

	Возвращает словарь:
	- ключи: имена интерфейсов, вида 'FastEthernet0/1'
	- значения: список команд, который надо выполнить на этом интерфейсе
	'''
	trunk_template = [
		'switchport trunk encapsulation dot1q', 'switchport mode trunk',
		'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
	]
	result_dict = {}
	result = []
	for interface, vlans in trunk.items():
		for command in trunk_template:
			if command.endswith('allowed vlan'):
				result.append('{} {}'.format(command, ', '.join([str(vlan) for vlan in vlans])))
			else:
				result.append(command)
		result_dict[interface] = result
	print(result_dict)


trunk_dict = {
	'FastEthernet0/1': [10, 20, 30],
	'FastEthernet0/2': [11, 30],
	'FastEthernet0/4': [17]
}

generate_trunk_config(trunk_dict)
