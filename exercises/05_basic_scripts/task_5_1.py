#!/usr/bin/env python3

"""
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24/n

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

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

print(pr.format(int(IP[0]), int(IP[1]), int(IP[2]), int(IP[3]), maska,  MASK1, MASK2, MASK3, MASK4))
