import os

directory_list = list()
for root, dirs, files in os.walk("A_Comprimir/", topdown=False):
    for name in dirs:
        directory_list.append(os.path.join(root, name))

print(directory_list)