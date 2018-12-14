#!/usr/bin/env python3

import os
import sqlite3
import yaml
import re
from datetime import timedelta, datetime
from operator import itemgetter

def create_db(db_filename, schema_filename):
	db_exists = os.path.exists(db_filename)
	conn = sqlite3.connect(db_filename)
	if not db_exists:
		print('Creating schema...')
		with open(schema_filename, 'r') as f:
			schema = f.read()
		conn.executescript(schema)
		print('Done')
	else:
		print('Database exists, assume dhcp table does, too.')

def get_data(db_filename, key, value):
	conn = sqlite3.connect(db_filename)
	keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active', 'time']
	conn = sqlite3.connect(db_filename)
	conn.row_factory = sqlite3.Row
	keys.remove(key)
	query = 'select * from dhcp where {} = ? order by active desc'.format(key)
	result = conn.execute(query, (value, ))
	for row in result:
		if row['active'] == 0:
			print('-'*40+'\nInactive values:\n'+'-'*40)
		for k in keys:
			print('{:12}: {}'.format(k, row[k]))
		print('-' * 40)

def get_all_data(db_filename):
	conn = sqlite3.connect(db_filename)
	query = 'select * from dhcp'
	result = [row for row in conn.execute(query)]
	result = sorted(result, key=itemgetter(5), reverse = True)
	print('Active values:\n'+'-'*40)
	for row in result:
		if row[5] == 0 and result[result.index(row)-1][5] == 1:
			print('-'*40+'\nInactive values:\n'+'-'*40)
		print('{:20}{:20}{:12}{:20}{:5}{:2}  {:15}'.format(*row))

def add_data_switches(db_filename, file_list):
	conn = sqlite3.connect(db_filename)
	for yaml_file in file_list:
		with open(yaml_file) as f:
			switches = yaml.load(f)
			print('Inserting Swithes data')
			for value in switches.values():
				for key1, value1 in value.items():
					try:
						with conn:
							query = 'REPLACE into switches values (?, ?)'
							conn.execute(query, (key1, value1,))

					except sqlite3.IntegrityError as e:
						print('Error occured: ', e)

def add_data(db_filename, file_list):
	result = []
	conn = sqlite3.connect(db_filename)
	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	query1 = 'UPDATE dhcp set active = 0 where not switch = 1'
	
	for fname in file_list:
		with open(fname) as data:
			switch = fname.split('_')[0]
			#print(switch)
			for line in data:
				match = regex.search(line)
				if match:
					f_list = list(match.groups())
					f_list.append(switch)
					result.append(tuple(f_list))
			conn.execute(query1)

	print('Inserting DHCP Snooping data')
	
	now = datetime.today().replace(microsecond=0)
	week_ago = now - timedelta(days=7)

	for row in result:
		try:
			with conn:
				query2 = 'REPLACE into dhcp values (?, ?, ?, ?, ?, 1, ?)'
				conn.execute(query2, (*row, now))

		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)
			
	query = 'DELETE from dhcp where time = ?'
	times = [row[-1] for row in conn.execute('SELECT * from dhcp')]
	for time in times:
		if str(time) < str(week_ago):
			conn.execute(query, (time,))
