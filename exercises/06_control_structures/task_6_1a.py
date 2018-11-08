#!/usr/bin/env python3
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
IP = input('Введите ip адрес (в виде 10.0.1.1): ')
IP_correct = True

if IP.count('.') == 3:
	for oktet in IP.split('.'):
		if oktet.isdigit() and 0 <= int(oktet) <= 255:
			pass
		else:
			IP_correct = False
			print('Incorrect IPv4 address')
else:
	IP_correct = False
	print('Incorrect IPv4 address')
if IP_correct:
	IP1 = int(IP.split('.')[0])
	if 0 < IP1 < 224:
		if 0 < IP1 < 128: 
			cls = 'A'
		elif 128 <= IP1 < 192:
			cls = 'B'
		elif 192<= IP1 < 224:
			cls = 'C'
		print('unicast /', cls)
	elif 224 <= IP1 < 240:
		cls = 'D'
		print('multicast', cls)
	elif IP == '255.255.255.255':
		print('local broadcast')
	elif IP == '0.0.0.0':
		print('unassigned')
	else:
		print('unused')
