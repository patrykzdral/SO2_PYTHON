#!/usr/bin/env python3
#
# Zadanie P6
# Patryk Zdral
# 20.04.2018 11:15 TP
#
#
import os
import sys

dict = {}
if sys.argv.__len__() != 2:
    print("Podano nieprawidłą ilość plików")
    sys.exit(1)
else:
    directory_path = sys.argv[1]
if not os.path.isdir(directory_path):
    print("ścieżka" + directory_path + " nie jest katalogiem")
    sys.exit(1)


def list_unique_files(path):
    for filename in os.listdir(path):
        if os.path.isdir(path + "/" + filename):
            list_unique_files(path + "/" + filename)
        else:
            if os.access(directory_path + "/" + filename, os.W_OK) and os.access(directory_path + "/" + filename,
                                                                                 os.R_OK):
                if dict.__contains__(filename):
                    dict.update({filename: 2})
                else:
                    dict.update({filename: 1})


list_unique_files(directory_path)
for k, v in dict.items():
    if (v == 1):
        print(k)
