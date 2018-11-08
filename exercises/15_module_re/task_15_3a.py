#!/usr/bin/env python3
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

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
					result_dict[intf] = ()
				else:
					result_dict[intf] = (match.group('ip'), match.group('mask'))

	keys = list(result_dict.keys())
	for key in keys:
		if result_dict[key] == ():
			del(result_dict[key])
	return result_dict

print(parse_cfg('config_r1.txt'))
