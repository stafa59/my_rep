#!/usr/bin/env python3
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

regex = ('interface (?P<intf>\S+)|ip address (?P<ip>[0-9|\.]+) *(?P<mask>[0-9|\.]+)')

def parse_cfg (file_in):
	result_dict = {}
	with open(file_in) as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				if match.lastgroup == 'intf':
					intf = match.group('intf')
					result_dict[intf] = []
				else:
					if result_dict[intf]:
						result_dict[intf] = [*result_dict[intf],(match.group('ip'), match.group('mask'))]
					else:
						result_dict[intf] = [(match.group('ip'), match.group('mask'))]

	keys = list(result_dict.keys())
	for key in keys:
		if result_dict[key] == []:
			del(result_dict[key])
	return result_dict

print(parse_cfg('config_r2.txt'))
