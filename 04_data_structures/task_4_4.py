# -*- coding: utf-8 -*-
"""
Задание 4.4

Список vlans это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка vlans нужно получить новый список уникальных номеров VLANов,
отсортированный по возрастанию номеров. Для получения итогового
списка нельзя удалять конкретные vlanы вручную.

Записать итоговый список уникальных номеров VLANов в переменную result.
(именно эта переменная будет проверяться в тесте)

Полученный список result вывести на стандартный поток вывода (stdout)
с помощью print.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = sorted (set (vlans))
print ( result )

