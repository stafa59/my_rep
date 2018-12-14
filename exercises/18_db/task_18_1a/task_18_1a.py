#!/usr/bin/env python3
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''

import glob
import sqlite3
import yaml
import re
import os

db_filename = 'db.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
yaml_file = 'switches.yml'
#print(dhcp_snoop_files)

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

result = []

def insert_dhcp(conn):
	for fname in dhcp_snoop_files:
		with open(fname) as data:
			for line in data:
				match = regex.search(line)
				if match:
					f_list = list(match.groups())
					f_list.append(fname.split('_')[0])
					result.append(tuple(f_list))

	print('Inserting DHCP Snooping data')

	for row in result:
		try:
			with conn:
				query = '''insert into dhcp values (?, ?, ?, ?, ?)'''
				conn.execute(query, row)
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
					query = '''insert into switches values (?, ?)'''
					conn.execute(query, (key1, value1,))
			except sqlite3.IntegrityError as e:
				print('Error occured: ', e)



if os.path.exists(db_filename):
	conn = sqlite3.connect(db_filename)
	insert_dhcp(conn)
	insert_switches(conn)
else:
	print('БД необходимо создать')
