import glob
import os
import sys

path = sys.argv[1]


# filename.endswith(".old")
def change_extension():
    if not os.path.isdir(path):
        print("ścieżka nie jest katalogiem")
        return 1
    old_list = glob.glob('{}/*.old'.format(path))
    for old in old_list:
        print(old)
        os.remove(old)
    for filename in os.listdir(path):
        print(path+"/"+filename)
        if os.access(path + "/" + filename, os.W_OK):
            os.rename(path+"/"+filename, path+"/"+filename+".old")

change_extension()
