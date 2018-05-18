#!/usr/bin/env python3
#
# Zadanie R3
# Patryk Zdral
# 18.05.2018 11:15 TP
#
#
import re
import subprocess

stdoutdata = subprocess.getoutput("df --block-size=1")
list = stdoutdata.split()
size = 0
pattern = '^/dev/*'
r = re.compile(pattern)
for i in range(7, len(list) - 7, 6):
    if r.match(list[i + 5]):
        size += int(list[i + 1])

print("LICZBA WOLNEJ PRZESTRZENI DYSKOWEJ:" + str(size))

