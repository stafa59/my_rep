#!/usr/bin/env python3
'''
Задание 18.5

Теперь в БД остается и старая информация.
И, если какой-то MAC-адрес не появлялся в новых записях, запись с ним,
может оставаться в БД очень долго.

И, хотя это может быть полезно, чтобы посмотреть, где MAC-адрес находился в последний раз,
постоянно хранить эту информацию не очень полезно.

Например, если запись в БД уже больше месяца, то её можно удалить.

Для того, чтобы сделать такой критерий, нужно ввести новое поле,
в которое будет записываться последнее время добавления записи.

Новое поле называется last_active и в нем должна находиться строка,
в формате: YYYY-MM-DD HH:MM:SS.

В этом задании необходимо:
* изменить, соответственно, таблицу dhcp и добавить новое поле.
 * таблицу можно поменять из cli sqlite, но файл dhcp_snooping_schema.sql тоже необходимо изменить
* изменить скрипт add_data.py, чтобы он добавлял к каждой записи время

Как получить строку со временем и датой, в указанном формате, показано в задании.
Раскомментируйте строку и посмотрите как она выглядит.

'''

#import datetime

#now = str(datetime.datetime.today().replace(microsecond=0))
##print(now)

from create_db import create
from add_data import insert_dhcp, insert_switches
import sqlite3

db_filename = 'db1.db'
shema_filename = 'dhcp_snooping_schema.sql'

conn = create(db_filename, shema_filename)
insert_dhcp(conn)
insert_switches(conn)

for tuples in conn.execute('select * from dhcp'):
	print('{:20}{:18}{:5}{:18}{:3} {:3}   {:15}'.format(*tuples))
