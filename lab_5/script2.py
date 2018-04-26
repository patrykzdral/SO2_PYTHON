import os
import sys

directory_path = sys.argv[1]
file_path = sys.argv[2]

# filename.endswith(".old")
def create_new_files():
    if not os.path.isfile(file_path):
        print("ścieżka" + file_path + " nie jest plikiem")
        return 1
    if not os.path.isdir(directory_path):
        print("ścieżka" + directory_path + " nie jest katalogiem")
        return 1

    file = open(file_path, 'r')
    file_text = file.read()
    words = list(file_text.split())
    print(words)

    for i in range(0, words.__len__()):
        f = open(directory_path + words[i], "w+")
        f.close()


create_new_files()
