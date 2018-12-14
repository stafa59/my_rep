#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Отправить команду command на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_show_command.

'''
import yaml
from netmiko import ConnectHandler

command = 'sh ip int br'

def send_show_command(file_in = 'devices.yaml'):
	with open(file_in) as f:
		devices = yaml.load(f)
		devices = list(devices.values())[0]
		#print(devices)
	
	for dct in devices:
		#print(dct)
		print('Connection to device {}'.format(dct['ip']))
		with ConnectHandler(**dct) as ssh:
			ssh.enable()
			result = ssh.send_command(command)
			print(result)

send_show_command()
