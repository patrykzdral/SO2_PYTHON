#!/usr/bin/env python3
#
# Zadanie Q3
# Patryk Zdral
# 20.04.2018 11:15 TP
#
#
import os
import random
import shutil
import sys

directiories = []
for i in range(1, sys.argv.__len__()):
    directiories.append(sys.argv[i])

for i in range(1, directiories.__len__()):
    if not os.path.isdir(directiories[i]):
        print("jeden z argumentów nie jest katalogiem")
        sys.exit(1)
    if not os.access(directiories[i], os.R_OK):
        print("Niepoprawne uprawninenia")
        sys.exit(1)


def filer_mover(number_of_moves):
    for i in range(0, number_of_moves):
        while True:
            dir_from = random.choice(directiories)
            dir_to = random.choice(directiories)
            if dir_from != dir_to:
                break
        for j in range(0, number_of_moves):
            file_list_from = get_new_list(dir_from)
            file_to = random.choice(file_list_from)
            if os.path.islink(dir_to + "/" + file_to):
                os.unlink(dir_to + "/" + file_to)

            shutil.move(dir_from + "/" + file_to, dir_to)
            os.symlink(dir_to + "/" + file_to, dir_from + "/" + file_to)


def get_new_list(dir):
    new_list = []
    for file_name in os.listdir(dir):
        if not os.path.islink(dir + "/" + file_name):
            new_list.append(file_name)
    return new_list


filer_mover(1)