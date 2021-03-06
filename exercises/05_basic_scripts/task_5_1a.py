#!/usr/bin/env python3
"""
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

pr = """
Network:
{0:8}  {1:8}  {2:8}  {3:8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4:}
{5:8}  {6:8}  {7:8}  {8:8}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
"""

inp = input('IP-сети и маска сети в формате: 10.1.1.0/24\n')
inp = inp.strip().split('/')
IP = inp[0].split('.')
maska = int(inp[1])

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
