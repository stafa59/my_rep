#!/usr/bin/env python3
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from draw_network_graph import draw_topology
from task_11_1 import parse_cdp_neighbors

file1 = open('sw1_sh_cdp_neighbors.txt')
file2 = open('sh_cdp_n_r1.txt')
file3 = open('sh_cdp_n_r2.txt')
file4 = open('sh_cdp_n_r3.txt')


file_list = list()

file_list.append(file1.read())
file_list.append(file2.read())
file_list.append(file3.read())
file_list.append(file4.read())


sum_dict = {}
for files in file_list:
	sum_dict.update(parse_cdp_neighbors(files))

print(sum_dict)
keys = list(sum_dict.keys())
for key in keys:
	for k in keys:
		if (sum_dict.get(key) == k) and (key in sum_dict.keys()):
			del(sum_dict[k])

print(sum_dict)
draw_topology(sum_dict)
