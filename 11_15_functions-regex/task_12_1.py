# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

ip_addresses = ("8.8.8.8","10.1.1.1", "172.217.18.78", "9.10.11.12") 

def ping_ip_addresses(ip_addresses):
    active = []
    unreach = []
    for address in ip_addresses:
        reply = subprocess.run(['ping', '-c', '3', '-n', address],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='utf-8')
        if reply.returncode == 0:
            active.append(address)
        else:
            unreach.append(address)
    return active,unreach

if __name__ == "__main__":
    print (ping_ip_addresses(ip_addresses))
