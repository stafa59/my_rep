#!/usr/bin/env python3
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

slovar1 = dict([('acess',['\n'.join(access_template), 'Enter VLAN number:']), 
         ('trunk',['\n'.join(trunk_template), 'Enter allowed VLANs:'])])
int_mode = input('Enter interface mode (access/trunk): ')
int_type = input('Enter interface type and number: ')
print(slovar1[int_mode][1], end = '')
vlan = input()
print()
print('interface {}'.format(int_type))
print(slovar1[int_mode][0].format(vlan))
