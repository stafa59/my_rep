#!/usr/bin/env python3
'''
На основе файла get_data_ver1.py из раздела, создать скрипт get_data.py.

Код в скрипте должен быть разбит на функции. Какие именно функции и как разделить код, надо решить самостоятельно. Часть кода может быть глобальной.

В примере из раздела, скрипту передавались два аргумента:

key - имя столбца, по которому надо найти информацию
value - значение
Теперь необходимо расширить функциональность таким образом:

если скрипт был вызван без аргументов, вывести всё содержимое таблицы dhcp более компактно (как в примере ниже)
если скрипт был вызван с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
если скрипт был вызван с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов
Обработка некорректного ввода аргумента будет выполняться в следующем задании

Файл БД можно скопировать из прошлых заданий

В итоге, вывод должен выглядеть так:

$ python get_data.py

В таблице dhcp такие записи:
----------------------------------------------------------------------
00:09:BB:3D:D6:58  10.1.10.2         10    FastEthernet0/1      sw1
00:04:A3:3E:5B:69  10.1.5.2          5     FastEthernet0/10     sw1
00:05:B3:7E:9B:60  10.1.5.4          5     FastEthernet0/9      sw1
00:07:BC:3F:A6:50  10.1.10.6         10    FastEthernet0/3      sw1
00:09:BC:3F:A6:50  192.168.1.100     100   FastEthernet0/5      sw1
00:A9:BB:3D:D6:58  10.1.10.20        10    FastEthernet0/7      sw2
00:B4:A3:3E:5B:69  10.1.5.20         5     FastEthernet0/5      sw2
00:C5:B3:7E:9B:60  10.1.5.40         5     FastEthernet0/9      sw2
00:A9:BC:3F:A6:50  100.1.1.6         3     FastEthernet0/20     sw3

$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------


$ python get_data.py vlan 10

Detailed information for host(s) with vlan 10
----------------------------------------
mac         : 00:09:BB:3D:D6:58
ip          : 10.1.10.2
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------
mac         : 00:07:BC:3F:A6:50
ip          : 10.1.10.6
interface   : FastEthernet0/3
switch      : sw1
----------------------------------------
mac         : 00:A9:BB:3D:D6:58
ip          : 10.1.10.20
interface   : FastEthernet0/7
switch      : sw2
----------------------------------------

$ python get_data.py vlan
Пожалуйста, введите два или ноль аргументов
'''

import sqlite3
import sys

db_filename = 'db.db'
keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
if len(sys.argv[1:]) == 2:
	key, value = sys.argv[1:]
	keys.remove(key)
conn = sqlite3.connect(db_filename)

def db_find(conn = conn, n = len(sys.argv[1:])):
	'''поиск по БД'''
	if n == 0:
		query = 'select * from dhcp'
		result = conn.execute(query)
		return result
	elif n == 2:
		#Позволяет далее обращаться к данным в колонках, по имени колонки
		conn.row_factory = sqlite3.Row
		query = 'select * from dhcp where {} = ?'.format(key)
		result = conn.execute(query, (value, ))
		return result


def output (result, n = len(sys.argv[1:])):
	if result:
		for row in result:
			if n == 2:
				for k in keys:
					print('{:12}: {}'.format(k, row[k]))
				print('-' * 40)
			elif n == 0:
				print('{:20}{:20}{:12}{:20}{:12}'.format(*row))
	else:
		print('неверное число аргументов')

print('-' * 40)
output(db_find())
