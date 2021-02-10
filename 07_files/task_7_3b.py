# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = input("Введите номер влана:")
file_name = "CAM_table.txt"
with open(file_name) as f:
    for line in f:
        if "." in line:
            temp = line.rstrip().replace("DYNAMIC","").split()
            if temp[0] == vlan:
                print(f"{temp[0]:9}",f"{temp[1]:20}",f"{temp[2]:6}")

