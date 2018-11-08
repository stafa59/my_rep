#!/usr/bin/env python3
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess

def check_ip_addresses(ip_list):
	"""
	Ping IP addresses and two lists:
	*available
	*unavailable
	"""
	available = []
	unavailable = []
	for ip in ip_list:
		reply = subprocess.run(['ping', '-c', '3', '-n', ip], 
								stdout = subprocess.PIPE,
								stderr = subprocess.PIPE,
								encoding='utf-8')
		
		if reply.returncode == 0 and reply.stdout.find('3 received'):
			available.append(ip)
		else:
			unavailable.append(ip)
	return available, unavailable
if __name__ == '__main__':
	print(check_ip_addresses(['8.8.8.8','192.169.10.5']))
