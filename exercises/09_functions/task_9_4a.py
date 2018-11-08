#!/usr/bin/env python3
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
	'''
	Функция проверяет содержится ли в команде слово из списка ignore.

	command - строка. Команда, которую надо проверить
	ignore - список. Список слов

	Возвращает True, если в команде содержится слово из списка ignore, False - если нет
	'''
	return any(word in command for word in ignore)

def set_command(config):
	'''
	Ожидается файл txt. Составляется словарь комманд
	'''
	with open(config) as file_input:
		command_dict = {}
		for line in file_input:
			if check_ignore(line, ignore) or line[0] == '!' or line[0] == '\n':
				pass
			else:
				if line[0] != ' ':
					key = line.rstrip()
					command_dict[key] = []
					contained_dict = {}
				else:
					if line[1] != ' ':
						key1 = line.rstrip()
						command_dict[key].append(key1)
					else:
						
						for contained_command in command_dict[key]:
							if contained_command == key1:
								if contained_dict.get(key1):
									contained_dict[contained_command].append(line.rstrip())
								else:
									contained_dict[contained_command] = [line.rstrip()]
							else:
								contained_dict[contained_command] = []
						command_dict[key] = contained_dict
						
		print (command_dict)

set_command('config_r1.txt')
