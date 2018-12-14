#!/usr/bin/env python3
'''
Задание 18.4

Обновить файл get_data из задания 18.2 или 18.2a.
Добавить поддержку столбца active, который мы добавили в задании 18.3.

Теперь, при запросе информации, сначала должны отображаться активные записи,
а затем, неактивные.

Например:
$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------

----------------------------------------
Inactive values:
----------------------------------------
mac         : 00:09:23:34:16:18
vlan        : 10
interface   : FastEthernet0/4
switch      : sw1
----------------------------------------

$ python get_data1.py
--------------------------------------------------------------------------------
Active values:
--------------------------------------------------------------------------------
00:09:BB:3D:D6:58  10.1.10.2         10    FastEthernet0/1    sw1         1
00:04:A3:3E:5B:69  10.1.5.2          5     FastEthernet0/10   sw1         1
00:05:B3:7E:9B:60  10.1.5.4          5     FastEthernet0/9    sw1         1
00:07:BC:3F:A6:50  10.1.10.6         10    FastEthernet0/3    sw1         1
00:09:BC:3F:A6:50  192.168.100.100   1     FastEthernet0/7    sw1         1
00:B4:A3:3E:5B:69  10.1.5.20         5     FastEthernet0/5    sw2         1
00:C5:B3:7E:9B:60  10.1.5.40         5     FastEthernet0/9    sw2         1
00:A9:BC:3F:A6:50  10.1.10.60        20    FastEthernet0/2    sw2         1
--------------------------------------------------------------------------------
Inactive values:
--------------------------------------------------------------------------------
00:A9:BB:3D:D6:58  10.1.10.20        10    FastEthernet0/7    sw2         0

'''

import sqlite3
import sys
from operator import itemgetter

db_filename = 'db.db'
keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active']
conn = sqlite3.connect(db_filename)

def db_find(conn = conn, n = len(sys.argv[1:])):
	'''поиск по БД'''
	if n == 0:
		query = 'select * from dhcp'
		result = conn.execute(query)
		result = [row for row in result]
		result = sorted(result, key=itemgetter(5), reverse = True)
	elif n == 2:
		#Позволяет далее обращаться к данным в колонках, по имени колонки
		conn.row_factory = sqlite3.Row
		query = 'select * from dhcp where {} = ? order by active desc'.format(key)
		result = conn.execute(query, (value, ))
	
	return result


def output (result, n = len(sys.argv[1:])):
	if result:
		if n == 2:
			print('Detailed information for host(s) with {} {}'.format(key, value))
			for row in result:
				if row['active'] == 0:
					print('-'*40+'\nInactive values:\n'+'-'*40)
				for k in keys:
					print('{:12}: {}'.format(k, row[k]))
				print('-' * 40)
		elif n == 0:
			print('Active values:\n'+'-'*40)
			for row in result:
				if row[5] == 0 and result[result.index(row)-1][5] == 1:
					print('-'*40+'\nInactive values:\n'+'-'*40)
				print('{:20}{:20}{:12}{:20}{:5}{:3}'.format(*row))
	else:
		print('неверное число аргументов')



if len(sys.argv[1:]) == 2:
	key, value = sys.argv[1:]
	
	
	if key in keys:
		keys.remove(key)
		output(db_find())
	else:
		print('Данный параметр не поддерживается.\n'
		'Допустимые значения параметров: {}, {}, {}, {}, {}'.format(*keys))
else:
	print('-' * 40)
	output(db_find())

conn.close()
