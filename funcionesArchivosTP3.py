##########################################################################
#Elaborado por: Mónica Alfaro Parrales y Jennifer Alvarado Brenes
#Inicio: 23/07/2020 16:20
#Última modificación: 03/08/2020 17:45
#Versión 3.8.2
##########################################################################

#Importación de librerías:

from personasClaseTP3 import *
import pickle
from tkinter import messagebox

##########################################################################

def graba(nomArchGrabar,lista):
    """
    Funcionalidad: Guardar los datos de lista de objetos en memoria secundaria del archivo binario.
    Entradas: El nombre del archivo y la lista de datos.
    Salidas: ---
    """
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        ""

def lee(nomArchLeer):
    """
    Funcionalidad: Leer los datos en memoria secundaria del archivo binario con la lista de objetos.
    Entradas: El nombre del archivo.
    Salidas: ---
    """
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        lista = pickle.load(f)
        f.close()
    except:
        ""
    return lista


def leer(nomArchLeer):
    """
    Funcionalidad: Leer los datos en memoria secundaria del archivo de texto con los funcionarios del TSE.
    Entradas: El nombre del archivo.
    Salidas: ---
    """
    try:
        registro=open(nomArchLeer,"r")
        listaDeFuncionarios=registro.readlines()
        if listaDeFuncionarios==" ":
            messagebox.showinfo(message="El registro de funcionarios parece estar vacío, contacte al soporte técnico.", title="Error")
        else:
            return listaDeFuncionarios
            
        registro.close()
    except:
        messagebox.showinfo(message="El registro de funcionarios parece estar vacío, contacte al soporte técnico.", title="Error")


