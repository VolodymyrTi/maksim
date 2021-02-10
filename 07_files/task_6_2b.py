# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите ip адрес :")
ip_address_correct = False

while not ip_address_correct:
    octet = ip.split(".")
    check = False

    if len(octet) == 4:
        for step in octet:
            check = True
            if not step.isdigit():
                check = False
                break
            elif not "0" <= step <= "255":
                check = False
                break
    if check:
        if ip == "0.0.0.0":
            print("unassigned")
            ip_address_correct = True
        elif ip == "255.255.255.255":
            print("local broadcast")
            ip_address_correct = True
        elif "1" <= octet[0] <= "223":
            print("unicast")
            ip_address_correct = True
        elif "224" <= octet[0] <= "239":
            print("multicast")
            ip_address_correct = True
        else:
            print("unused")
            ip_address_correct = True
    else:
        print ('Неправильный IP-адрес')
        ip = input("Введите ip адрес еще раз:")

