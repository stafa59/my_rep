#!/usr/bin/env python3
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает

Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

regex = ('IOS Software.+Version (?P<ios>\S+),'
		'|image file is "(?P<image>\S+)"'
		'|uptime is (?P<uptime>\d+ \w+(?:, \d+ \w+){2})')
data_list = []

def parse_sh_version (sh_version):
	rlist = [None, None, None, None]
	rlist[0] = sh_version.split('.')[0].split('_')[-1]
	with open(sh_version) as f:
		for line in f:
			match = re.search(regex, line)
			if match:
				if match.lastgroup == 'ios':
					rlist[1] = match.group('ios')
				elif match.lastgroup == 'image':
					rlist[2] = match.group('image')
				elif match.lastgroup == 'uptime':
					rlist[3] = match.group('uptime')
	return rlist

def write_to_csv (data, csv_out = 'routers_inventory.csv'):
	with open(csv_out, 'w') as f:
		writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
		writer.writerows(data)

for sh_version in sh_version_files:
	data_list.append(parse_sh_version(sh_version))

data_list = sorted(data_list)
write_to_csv(data_list)
