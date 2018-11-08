#!/usr/bin/env python3
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

from task_12_1 import check_ip_addresses

def check_ip_availability(ip):
	ip_list = []
	length1 = len(ip.split('-'))
	if length1 == 1:
		ip_list.append(ip)
	elif length1 == 2:
		if len(ip.split('-')[1]) > 3:
			ip_list = ['{}.{}.{}.{}'.format(*(ip.split('.')[0:3]), str(num))  
			for num in range(int(ip.split('-')[0].split('.')[-1]), int(ip.split('.')[-1]) + 1)]
			
		else:
			ip_list = ['{}.{}.{}.{}'.format(*(ip.split('.')[0:3]), str(num))  
			for num in range(int(ip.split('-')[0].split('.')[-1]), int(ip.split('-')[-1]) + 1)]
	return check_ip_addresses(ip_list)

if __name__ == '__main__':
	print(check_ip_availability('10.1.1.1-3'))
