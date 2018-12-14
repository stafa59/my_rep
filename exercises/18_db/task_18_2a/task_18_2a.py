#!/usr/bin/env python3
'''
Задание 18.2a

Дополнить скрипт get_data.py из задания 18.2

Теперь должна выполняться проверка не только по количеству аргументов,
но и по значению аргументов.
Если имя аргумента введено неправильно, надо вывести сообщение об ошибке
(пример сообщения ниже).

Файл БД можно скопировать из прошлых заданий

В итоге, вывод должен выглядеть так:

$ python get_data_ver1.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch

'''
import sqlite3
import sys

db_filename = 'db.db'
keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
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



if len(sys.argv[1:]) == 2:
	key, value = sys.argv[1:]
	if key in keys:
		keys.remove(key)
		print('-' * 40)
		output(db_find())
	else:
		print('Данный параметр не поддерживается.\n'
		'Допустимые значения параметров: {}, {}, {}, {}, {}'.format(*keys))
else:
	print('-' * 40)
	output(db_find())

conn.close()
