#!/usr/bin/env python3
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv
"""inp = input('IP-сети и маска сети в формате: 10.1.1.0/24\n')
inp = inp.strip().split('/')
IP = inp[0].split('.')
maska = int(inp[1])"""
IP, maska = argv[1:]

IP = IP.split('.')
MA = [ '1' for i in range(maska)]
SK = [ '0' for i in range(32-maska)]
MASK = MA + SK
MASK = ''.join(MASK)
MASK1 = int(MASK[:8],2)
MASK2 = int(MASK[8:16],2)
MASK3 = int(MASK[16:24],2)
MASK4 = int(MASK[24:],2)

IP[0] = '{:08b}'.format(int(IP[0]))
IP[1] = '{:08b}'.format(int(IP[1]))
IP[2] = '{:08b}'.format(int(IP[2]))
IP[3] = '{:08b}'.format(int(IP[3]))

SK = ''.join(SK)
IPs = ''.join(IP)
IPstr = IPs[:maska] + SK

IP1 = int(IPstr[:8],2)
IP2 = int(IPstr[8:16],2)
IP3 = int(IPstr[16:24],2)
IP4 = int(IPstr[24:],2)

print(pr.format(IP1, IP2, IP3, IP4, maska,  MASK1, MASK2, MASK3, MASK4))
