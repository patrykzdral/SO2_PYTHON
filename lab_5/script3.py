#!/usr/bin/env python3

import os
import sys

def rm_rf(d):
    for path in (os.path.join(d, f) for f in os.listdir(d)):
        if os.path.isdir(path):
            rm_rf(path)
        else:
            os.unlink(path)
    os.rmdir(d)


def remove_files():
    if sys.argv.__len__() != 2:
        print("Podano nieprawidłą ilość plików")
        sys.exit(1)
    else:
        directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("ścieżka" + directory_path + " nie jest katalogiem")
        sys.exit(1)

    for file_name in os.listdir(directory_path):
        if not os.access(directory_path + "/" + file_name, os.X_OK):
            if os.path.isdir(directory_path + "/" + file_name):
                print(directory_path + "/" + file_name)
                st = os.stat(directory_path + "/" + file_name)
                os.chmod(directory_path + "/" + file_name, st.st_mode | 0o111)
                rm_rf(directory_path + "/" + file_name)
            else:
                os.remove(directory_path + "/" + file_name)


remove_files()
