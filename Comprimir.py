import py7zr
import os
import shutil
import pathlib
from tkinter import messagebox

ruta = pathlib.Path(__file__).parent.absolute()

def Comprimir():
    for root, dirs, files in os.walk("A_Comprimir/", topdown=True):
        for name in dirs:
            shutil.move("A_Comprimir/" + name, ruta)
            print("Procesando: " + name)
            with py7zr.SevenZipFile(os.path.join("Comprimidos", name + ".7z"), 'w') as archive:
                archive.writeall(name)

def Borrar():
    for root, dirs, files in os.walk(ruta, topdown=True):
        for name in dirs:
            if name != ".idea" and name != "A_Comprimir" and name != "Comprimidos":
                shutil.rmtree(os.path.join(ruta,name), ignore_errors=True)

print("Trabajando ... ")
Comprimir()
Borrar()
print("Rutina Terminada")
messagebox.showinfo("Rutina Terminada","Carpetas comprimidas")


