#!/usr/bin/env python3
'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from draw_network_graph import draw_topology
from task_17_2b import topology_dict

topology = {}
for key, value in topology_dict.items():
	for key1, value1 in value.items():
		for key2, value2 in value1.items():
			topology.update({(key, key1):(key2, value2)})

for value in list(topology.values()):
	if topology[value] in topology.keys():
		del(topology[value])

print(topology)
draw_topology(topology)
