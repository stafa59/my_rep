#!/usr/bin/env python3
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import glob
import sqlite3
import yaml
import re
import datetime


dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
yaml_file = 'switches.yml'
#print(dhcp_snoop_files)

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

result = []

def insert_dhcp(conn):
	
	now = str(datetime.datetime.today().replace(microsecond=0))
	#print(now)
	
	query1 = 'UPDATE dhcp set active = 0 where switch = ?'
	
	for fname in dhcp_snoop_files:
		with open(fname) as data:
			switch = fname.split('_')[0]
			#print(switch)
			for line in data:
				match = regex.search(line)
				if match:
					f_list = list(match.groups())
					f_list.append(switch)
					result.append(tuple(f_list))
			conn.execute(query1, (switch,))

	print('Inserting DHCP Snooping data')
	#for row in conn.execute('SELECT * from dhcp'):
		#print(row)
	
	for row in result:
		try:
			with conn:
				query2 = 'REPLACE into dhcp values (?, ?, ?, ?, ?, 1, ?)'
				conn.execute(query2, (*row, now))

		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)

def insert_switches(conn):
	print('Inserting switches data')
	with open(yaml_file) as f:
		switches = yaml.load(f)
	
	for value in switches.values():
		for key1, value1 in value.items():
			try:
				with conn:
					query = 'REPLACE into switches values (?, ?)'
					conn.execute(query, (key1, value1,))

			except sqlite3.IntegrityError as e:
				print('Error occured: ', e)
