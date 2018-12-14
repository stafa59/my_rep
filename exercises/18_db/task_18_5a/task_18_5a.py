#!/usr/bin/env python3
'''
Задание 18.5a

После выполнения задания 18.5, в таблице dhcp есть новое поле last_active.

Обновите скрипт add_data.py, таким образом, чтобы он удалял все записи,
которые были активными более 7 дней назад.

Для того, чтобы получить такие записи, можно просто вручную обновить поле last_active.

В файле задания описан пример работы с объектами модуля datetime.
Обратите внимание, что объекты, как и строки с датой, которые пишутся в БД,
можно сравнивать между собой.

'''

from add_data import insert_dhcp, insert_switches, delete
import sqlite3

db_filename = 'db1.db'
shema_filename = 'dhcp_snooping_schema.sql'

conn = sqlite3.connect(db_filename)
insert_dhcp(conn)
#insert_switches(conn)
delete(conn)

for tuples in conn.execute('select * from dhcp'):
	print('{:20}{:18}{:5}{:18}{:3} {:3}   {:15}'.format(*tuples))
