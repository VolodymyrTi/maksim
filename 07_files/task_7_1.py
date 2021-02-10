# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ospf_template = [
     "Prefix                ",
     "AD/Metric             ",
     "Next-Hop              ",
     "Last update           ",
     "Outbound Interface    "
 ]

with open("ospf.txt") as file_str:
    for line in file_str:
        words = line.split()
        metric = words[2].strip("[]")
        hop = words[4].replace(",","")
        last = words[5].replace(",","")
        print(f" {ospf_template[0]} {words[1]}")
        print(f" {ospf_template[1]} {metric}")
        print(f" {ospf_template[2]} {hop}")
        print(f" {ospf_template[3]} {last}")
        print(f" {ospf_template[4]} {words[6]}")
