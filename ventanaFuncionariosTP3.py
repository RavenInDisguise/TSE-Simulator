##################################################################################
#Elaborado por Mónica Alfaro P y Jennifer Alvarado B
#Inicio 27/07/2020 15:00
#Última modificación 08/08/2020 21:50
#Versión 3.8.2
##################################################################################

#Importación de librerías:

from validacionesTP3 import *
from funcionesArchivosTP3 import *
from personasClaseTP3 import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.ttk as t
import webbrowser

##################################################################################

#Variables globales:

archivo="funcionariosRC.txt"
archivo1="Personas"
listaPersonas=[]
persona=Persona()
provinciasDicc={1:"San José",2:"Alajuela",3:"Cartago",4:"Heredia",5:"Guanacaste",6:"Puntarenas",7:"Limón",8:"Nacionalizado",9:"Partida especial de nacimientos"}
meses=list(range(1,13))
dias=list(range(1,32))
numAnnos=list(range(1955,2021))
nacionalidadMujer=["Costarricense","Alemana","Nicaragüense","Estadounidense","Colombiana"]
nacionalidadHombre=["Costarricense","Alemán","Nicaragüense","Estadounidense","Colombiano"]

##################################################################################

#Validaciones generales:

def validarCedula(cedula,cedula1,cedula2,cedula3):
    """
    Funcionalidad: Validar que el formato de la cédula ingresado sea correcto.
    Entradas: Cédula.
    Salidas: True o False y la cédula.
    """
    if(cedula.isdigit()):
        if(len(cedula)==9 and len(cedula1)==1 and len(cedula2)==4 and len(cedula3)==4):
            if(0<int(cedula1)<=9):
                cedula2=cedula1+"-"+cedula2+"-"+cedula3
                return True,cedula2
            else:
                messagebox.showinfo(message="La cédula debe poseer el primer dígito mayor a 0.", title="Error")
        else:
            messagebox.showinfo(message="El formato de ingreso debe ser el siguiente #-####-####", title="Error")
    else:
        messagebox.showinfo(message="Ingrese una cédula únicamente con números.", title="Error")


def validarExistencia(cedula):
    """
    Funcionalidad: Validar que la cédula esté registrada.
    Entradas: Cédula.
    Salidas: True (sí se encuentra) o False (no se encuentra).
    """
    for persona in listaPersonas:
        if(persona.obtenerCedula()==cedula):
            messagebox.showinfo(message="Ya existe una persona que posee esa cédula.", title="Error")
            return False
    return True

def validarExistencia2(cedula):
    """
    Funcionalidad: Validar que la cédula esté registrada.
    Entradas: Cédula.
    Salidas: True (sí se encuentra) o False (no se encuentra).
    """
    for persona in listaPersonas:
        if(persona.obtenerCedula()==cedula):
            return True
    messagebox.showinfo(message="No existe una persona que posea esa cédula.", title="Error")
    return False
##################################################################################

#Funciones generales:

##################################################################################

#Generar la ventana del certificado de nacimiento:

#Funciones generales de la ventana 5:

def generarVentanaCertificado():
        """
        Funcionalidad: Genera la ventana del certificado. 
        Entradas: Ninguna.
        Salidas: La ventana generada.
        """
##################################################################################

        #Validaciones ventana 5:
        
        def validarExistenciaPadres(dato):
                """
                Funcionalidad: Detectar si el dato del padre registrado es un guión. 
                Entradas: Dato.
                Salidas: True/False.
                """
                if dato=="-":
                    return True
                return False
        
        def obtenerNombresPadres(cedula):
                """
                Funcionalidad: Obtener el nombre de los padres.
                Entradas: La cédula de la madre o el padre.
                Salidas: El nombre de la persona.
                """
                for persona in listaPersonas:
                    if(persona.obtenerCedula()==cedula):
                            nombre=persona.obtenerNombre()
                            return nombre
                        
        def generarListaDatos(cedula):
                """
                Funcionalidad: Generar una lista con los elementos a mostrar en el HTML y el XML.
                Entradas: La cédula.
                Salidas: La lista con los elementos.
                """
                for persona in listaPersonas:
                        if(persona.obtenerCedula()==cedula):
                                datos=persona.obtenerTodo()#Cedula,nombre,sexo,ubicacion,fecha,padre,nacionalidad,madre,nacionalidad
                                if validarExistenciaPadres(datos[5]):
                                    nombrePadre=datos[5]
                                    nombreMadre=datos[7]
                                else:
                                    nombrePadre=obtenerNombresPadres(datos[5])
                                    nombreMadre=obtenerNombresPadres(datos[7])
                                nacioPa=datos[6]
                                nacioMa=datos[8]
                                if datos[2]=="F":
                                        sexo="Femenino"
                                else:
                                        sexo="Masculino"
                                tomo=["Tomo:",cedula[2:6]]
                                asiento=["Asiento:",cedula[7:]]
                                cita=["Cita:",cedula]
                                dice=["Nombre:",datos[1]]
                                sexo=["Sexo:",sexo]
                                nacioEn=["Nació en:",datos[3]]
                                fecha=["El día:",datos[4]]
                                padre=["Padre:",nombrePadre]
                                nacioP=["Nacionalidad:",nacioPa]
                                madre=["Madre:",nombreMadre]
                                nacioM=["Nacionalidad:",nacioMa]
                                elementos=[tomo,asiento,cita,dice,sexo,nacioEn,fecha,padre,nacioP,madre,nacioM]
                                return elementos
                        
        def generarHTML(elementos):
                """
                Funcionalidad: Generar el HTML.
                Entradas: La lista de datos.
                Salidas: El HTML.
                """
                nombreArchivo="certificado-"+elementos[2][1]+".html"
                f = open(nombreArchivo,'w')
                txtHTML="""<html lang="es">
                <head>
                <title>Certificado de Nacimiento</title>
                <meta http-equiv='Content-Type' content='text/html; charset=iso-8859-1' >
                <link rel="stylesheet" href="estilos.css"/>
                </head>
                <style type="text/css">
                table, th, td {border: 1px solid black;border-collapse: collapse;;}
                </style>
                <body>
                <table style="width: 100%">
                <th colspan="2"><h3>Certificado de Nacimiento</h3></th>"""
                for elemento in elementos:
                        txtHTML+="""
                        <tr><td align="center"><b>"""+elemento[0]+"""</b></td><td align="left">"""+elemento[1]+"""</td></tr>"""
                txtHTML+="""</table></body></html>"""
                f.write(txtHTML)
                f.close()
                webbrowser.open_new_tab(nombreArchivo)
                return
            
        def generarXML(elementos):
                """
                Funcionalidad: Generar el XML.
                Entradas: La lista de datos.
                Salidas: El XML.
                """
                nombreAr="certificado-"+elementos[2][1]+".xml"
                f=open(nombreAr,"w")
                txtXML="""<?xml version="1.0" encoding="iso-8859-1"?>
        <certificado>"""
                for elemento in elementos:
                        txtXML=txtXML+"""
                <dato>
                        <Elemento>"""+elemento[0]+"""</Elemento>
                        <Dato>"""+elemento[1]+"""</Dato>
                </dato>
        """
                txtXML=txtXML+"""</certificado>"""
                f.write(txtXML)
                f.close()
                webbrowser.open_new_tab(nombreAr)
                return
        def generarCertificados():
            """
            Funcionalidad: Indicar los HTML y XML.
            Entradas: El número de cédula.
            Salidas: El HTML y el XML.
            """
            try:
                cedula=entryCita1.get()+entryCita2.get()+entryCita3.get()
                cedula1=entryCita1.get()
                cedula2=entryCita2.get()
                cedula3=entryCita3.get()
                valor=validarCedula(cedula,cedula1,cedula2,cedula3)
                if(valor[0]==True):
                    if(validarExistencia2(valor[1])):
                        cedula=valor[1]
                        lista=generarListaDatos(cedula)
                        generarHTML(lista)
                        generarXML(lista)
            except:
                ""
                
        def limpiar3():
            """
            Funcionalidad: Borrar lo datos de los entrey's.
            Entradas: No hay.
            Salidas: Entry's vacíos.
            """
            entryCita1.delete(0,END)
            entryCita2.delete(0,END)
            entryCita3.delete(0,END)

        def regresar3():
            """
            Funcionalidad: Regresar a la ventana anterior.
            Entradas: Ventana actual.
            Salidas: Ventana del menú.
            """
            ventana5.destroy()
            menuPrincipal()

##################################################################################
            
        #Definición de la ventana 5:

        global listaPersonas
        listaPersonas=lee("Personas") 
        ventana5=Tk()
        ventana5.title("Certificado de nacimiento")
        ventana5.resizable(False, False)
        window_height = 200
        window_width = 500
        screen_width = ventana5.winfo_screenwidth()
        screen_height = ventana5.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        ventana5.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        ventana5.configure(background="white")
        labelTitulo3= Label(ventana5, text="Generar certificado de nacimiento",bg="white",font=("Arial Bold",14,"bold"))
        labelTitulo3.place(x=100, y=10)
        labelCedula= Label(ventana5, text="Cédula:",bg="white")
        labelCedula.place(x=70, y=55)
        entryCita1 = ttk.Entry(ventana5,width=1)
        entryCita1.place(x=175, y=55)
        labelGuion= Label(ventana5, text="-",bg="white",font=("Arial Bold",12,))
        labelGuion.place(x=200, y=55)
        entryCita2=ttk.Entry(ventana5,width=4)
        entryCita2.place(x=225, y=55)
        labelGuion= Label(ventana5, text="-",bg="white",font=("Arial Bold",12,))
        labelGuion.place(x=265, y=55)
        entryCita3=ttk.Entry(ventana5,width=4)
        entryCita3.place(x=285, y=55)
        botonCertificado=Button(ventana5, text="Generar certificado", height=2, width=20,command=generarCertificados)
        botonCertificado.place(x=70, y=100)
        botonLimpio3=Button(ventana5, text="Limpiar", height=2, width=10, command=limpiar3)
        botonLimpio3.place(x=235, y=100)
        botonRegresar3=Button(ventana5, text="Regresar", height=2, width=10, command=regresar3)
        botonRegresar3.place(x=330, y=100)

def generarVentana5(ventana2):
    """
    Funcionalidad: Generar la ventana.
    Entradas: La ventana2 (el menú principal).
    Salidas: Ninguna.
    """
    ventana2.destroy()
    #Llamada a la generación de la ventana:
    generarVentanaCertificado()
        
##################################################################################
    
#Generar la ventana del árbol genealógico:

#Funciones generales de la ventana 4:

def generarVentanaArbol():
    """
    Funcionalidad: Generar la ventana 4.
    Entradas: Ninguna.
    Salidas: Ninguna.
    """
    def encontrarPadres():
        """
        Funcionalidad: Encontrar la cédula de los padres de la persona.
        Entradas: Ninguna.
        Salidas: Ninguna.
        """
        try:
            datosPersona=persona.get()
            datosPersona=datosPersona.split()
            for personas in listaPersonas:
                cedula=personas.obtenerCedula()
                if(cedula==datosPersona[0]):
                    padre=personas.obtenerPadre()
                    madre=personas.obtenerMadre()
                    nombre=personas.obtenerNombre()
                    labelText3.set(nombre)
            return madre,padre
        except:
             messagebox.showinfo(message="Escoja una opción del selector.", title="Error")
            

    def generarArbol():
        """
        Funcionalidad: Cambiar los labels con los nombres de los padres y el hijo.
        Entradas: Ninguna.
        Salidas: Ninguna.
        """
        try:
            salida=encontrarPadres()
            cedulaM=salida[0]
            cedulaH=salida[1]
            for personas in listaPersonas:
                cedula=personas.obtenerCedula()
                if(cedulaM==cedula):
                    nombreM=personas.obtenerNombre()
                    labelText2.set(nombreM)
                if(cedulaH==cedula):
                    nombreH=personas.obtenerNombre()
                    labelText.set(nombreH)
                if(cedulaM=="-"):
                    labelText2.set("-")
                if(cedulaH=="-"):
                    labelText.set("-")
                else:
                    continue
        except:
            ""
        
    def limpiar2():
        """
        Funcionalidad: Borrar lo datos de los labels y el combobox.
        Entradas: No hay.
        Salidas: labels y el combobox vacíos.
        """
        labelText.set("-")
        labelText2.set("-")
        labelText3.set("-")
        persona.set("")
        
    def regresarMenu2():
        """
        Funcionalidad: Regresar a la ventana anterior.
        Entradas: Ventana actual.
        Salidas: Ventana del menú.
        """
        ventana4.destroy()
        menuPrincipal()
        

    def encontrarUsuarios():
        """
        Funcionalidad: Encontrar el nombre del hijo.
        Entradas: Ninguna.
        Salidas: La lista con la cédula y el nombre de todos los usuarios la lista list(listaArbol).
        """
        listaArbol=[]
        for persona in listaPersonas:
            cedula=persona.obtenerCedula()
            nombre=persona.obtenerNombre()
            opcion=cedula+" "+nombre
            listaArbol.append(opcion)
        return listaArbol

    def datosPersona(event):
        """
        Funcionalidad: Obtener el dato seleccionado en el combobox de Madre.
        Entradas: Evento del combobox.
        Salidas: El dato.
        """
        datosPersona=persona.get()
        return datosPersona

##################################################################################
            
    #Definición de la ventana 4:

    global listaPersonas
    listaPersonas=lee("Personas")
    ventana4=Tk()
    ventana4.title("Árbol genealógico")
    ventana4.resizable(False, False)
    window_height = 400
    window_width = 500
    screen_width = ventana4.winfo_screenwidth()
    screen_height = ventana4.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    ventana4.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ventana4.configure(background="white")
    labelTitulo2= Label(ventana4, text="Mostrar árbol genealógico",bg="white",font=("Arial Bold",14,"bold"))
    labelTitulo2.place(x=130, y=15)
    labelPersona= Label(ventana4, text="Persona:",bg="white",font=("Arial Bold",12,))
    labelPersona.place(x=40, y=60)
    salida=encontrarUsuarios()
    persona=t.Combobox(ventana4,width=47,values=salida, state='readonly')
    persona.place(x=120,y=60)
    persona.bind("<<ComboboxSelected>>",datosPersona)
    botonMostrar=Button(ventana4, text="Mostrar", height=2, width=10,command=generarArbol)
    botonMostrar.place(x=110, y=100)
    botonLimpio=Button(ventana4, text="Limpiar", height=2, width=10, command=limpiar2)
    botonLimpio.place(x=220, y=100)
    botonRegresar2=Button(ventana4, text="Regresar", height=2, width=10,command=regresarMenu2)
    botonRegresar2.place(x=330, y=100)
    labelSubtitulo= Label(ventana4, text="Resultados de la búsqueda:",bg="white",font=("Arial Bold",12,))
    labelSubtitulo.place(x=40, y=165)
    labelText=StringVar()
    labelText.set("-")
    labelPadre= Label(ventana4, textvariable=labelText, borderwidth=2, relief="groove",bg="white",font=("Arial Bold",12,))
    labelPadre.place(x=40, y=210)
    labelText2=StringVar()
    labelText2.set("-")
    labelMadre= Label(ventana4, textvariable=labelText2, borderwidth=2, relief="groove",bg="white",font=("Arial Bold",12,))
    labelMadre.place(x=300, y=210)
    labelText3=StringVar()
    labelText3.set("-")
    labelHijo= Label(ventana4, textvariable=labelText3, borderwidth=2, relief="groove",bg="white",font=("Arial Bold",12,))
    labelHijo.place(x=160, y=340)
    canvas1 = Canvas(width=100, height=100,bg="white",highlightthickness=0)
    canvas1.place(x=90,y=235)
    canvas1.create_line(10, 10, 80, 80)
    canvas2 = Canvas(width=100, height=100,bg="white",highlightthickness=0)
    canvas2.place(x=300,y=235)
    canvas2.create_line(10, 80, 80, 10)

def generarVentana4(ventana2):
    """
    Funcionalidad: Generar la ventana.
    Entradas: La ventana2 (el menú principal).
    Salidas: Ninguna.
    """
    ventana2.destroy()
    #Llamada a la generación de la ventana:
    generarVentanaArbol()

##################################################################################

#Generar la ventana de registro:

def generarVentana3():

##################################################################################

    #Validaciones de la ventana 3:
    
    def esBisiesto(anno):
        """
        Funcionalidad: Validar si el año es bisiesto.
        Entradas: El número del año.
        Salidas: True (es bisiesto) o False (no es bisiesto).
        """
        if(anno%4==0 and (anno%100!=0 or anno%400==0)):
           return True
        return False
    
    def validarProvincia(provincia):
        """
        Funcionalidad: Validar que los datos para definir la provincia estén bien.
        Entradas: El label de la provincia.
        Salidas: True (es correcta) o False (no es correcta).
        """
        if (provincia=="Ninguna" or provincia=="Cédula ingresada incorrectamente"):
            return False
        return True

    def validarLargoApellido(apellido):
        """
        Funcionalidad: Validar que se hayan ingresado 2 apellidos.
        Entradas: Lo ingresado en apellidos.
        Salidas: True (son correctos) o False (no son correctos).
        """
        apellido=apellido.split()
        if (len(apellido)==2):
            return True
        else:
            messagebox.showinfo(message="Ingrese dos apellidos", title="Error")
            return False

    def validarPalabras(pvariable):
        """
        Funcionalidad: Validar que las cajas de texto tengan datos..
        Entradas: Lo ingresado en las cajas de texto.
        Salidas: True (sí tiene datos) o False (no tiene datos).
        """
        pvariable=pvariable.lower()
        for valor in pvariable:
            if(re.match("([0-9]|[^a-zA-z ´ á é í ó ú ñ])",valor)):
                messagebox.showinfo(message="Ingrese únicamente valores alfabéticos.", title="Error")
                return False
        if(pvariable.isspace() or pvariable==""):
            messagebox.showinfo(message="Escriba al menos un valor en las cajas de texto.", title="Error")
            return False    
        return True

    def validarPalabras2(pvariable):
        """
        Funcionalidad: Validar que las cajas de texto tengan datos..
        Entradas: Lo ingresado en las cajas de texto.
        Salidas: True (sí tiene datos) o False (no tiene datos).
        """
        pvariable=pvariable.lower()
        for valor in pvariable:
            if(re.match("([^a-zA-Z0-9 ´ á é í ó ú ñ])",valor)):
                messagebox.showinfo(message="Ingrese únicamente valores alfabéticos.", title="Error")
                return False
        if(pvariable.isspace() or pvariable==""):
            messagebox.showinfo(message="Escriba al menos un valor en las cajas de texto.", title="Error")
            return False    
        return True

    def validarFecha(anno,mes,dia):
        """
        Funcionalidad: Revisar que la fecha ingresada sea válida.
        Entradas: Los números de año, mes y día.
        Salidas: True (es correcta) o False (no es correcta).
        """
        anno=int(anno)
        mes=int(mes)
        dia=int(dia)
        if esBisiesto(anno):
            if mes==2:
                if dia in range(1,30):
                    return True
                else:
                    messagebox.showinfo(message="Ingrese un día válido para Febrero en un año bisiesto (del 1 al 29).", title="Error")
                    return False
        else:
            if mes==2:
                if dia in range(1,29):
                    return True
                else:
                    messagebox.showinfo(message="Ingrese un día válido para Febrero en un año normal (del 1 al 28).", title="Error")
                    return False
        if mes==4 or mes==6 or mes==9 or mes==11:
            if dia in range(1,31):
                return True
            else:
                messagebox.showinfo(message="Ingrese un día entre 1 y 30 para los meses de abril, junio, setiembre o noviembre.", title="Error")
                return False
        else:
            if dia in range(1,32):
                return True
            else:
                messagebox.showinfo(message="Ingrese un día entre 1 y 31 para los meses de enero, marzo, mayo, julio, agosto, octubre o diciembre.", title="Error")
                return False

    def validarPadres(apellidos,nombrePadre,nombreMadre):
        """
        Funcionalidad: Revisar que los apellidos de la persona y los padres sean compatibles.
        Entradas: Los apellidos de la persona y los nombres completos de ambos padres.
        Salidas: True (es compatible) o False (no es compatible).
        """
        apellidos=apellidos.lower()
        nombrePadre=nombrePadre.lower()
        nombreMadre=nombreMadre.lower()
        nombrePa=nombrePadre.split(" ")
        if len(nombrePa)==5:
            apellido1=nombrePa[3]
        else:
            apellido1=nombrePa[2]
        nombreMa=nombreMadre.split(" ")
        if len(nombreMa)==5:
            apellido2=nombreMa[3]
        else:
            apellido2=nombreMa[2]
        apellidosP=apellidos.split(" ")
        apePer1=apellidosP[0]
        apePer2=apellidosP[1]
        if apePer1==apellido1 and apePer2==apellido2:
            return True
        else:
            messagebox.showinfo(message="El parentesco no es compatible entre apellidos.", title="Error")

    def validarSelectores(dato):
        """
        Funcionalidad: Revisar que los combobox no estén vacíos.
        Entradas: El dato del combobox.
        Salidas: True (no está vacío) o False (está vacío).
        """
        if dato=="":
             messagebox.showinfo(message="Escoja una opción en los selectores.", title="Error")
             return False
        return True
    
##################################################################################

   #Funciones generales de la ventana 3:

    def definirFecha(anno,mes,dia):
        """
        Funcionalidad: Formar un str con el formato de la fecha.
        Entradas: Números que indican el año, mes y días.
        Salidas: Str con la fecha y el formato dd/mm/aaaa.
        """
        if len(mes)==1:
            mes="0"+mes
        if len(dia)==1:
            dia="0"+dia
        fechaNacimiento=dia+"/"+mes+"/"+anno
        return fechaNacimiento
    
    def definirDistritoCanton(distrito,canton,provincia):
        """
        Funcionalidad: Generar el lugar con distrito, cantón y provincia juntos.
        Entradas: Nombres de distrito, cantón y provincia.
        Salidas: Str con el lugar.
        """
        distrito=distrito.title()
        canton=canton.title()
        nombreLugar=distrito+", "+canton+", "+provincia
        return nombreLugar
        
    def definirNombre(nombre,apellidos):
        """
        Funcionalidad: Formar un str con el nombre y los apellidos.
        Entradas: Nombre y apellidos.
        Salidas: Str con el nombre completo.
        """
        nombre=nombre.title()
        apellidos=apellidos.title()
        nombrePersona=nombre+" "+apellidos
        return nombrePersona

    def asignarDatos(cedula,nombre,genero,lugar,fecha,datoPadre,datoNaPa,datoMadre,datoNaMa):
        """
        Funcionalidad: Asignar cada dato a su respectivo atributo dentro de la clase.
        Entradas: Los datos.
        Salidas: La lista con la persona agregada.
        """
        persona.asignarCedula(cedula)
        persona.asignarNombre(nombre)
        persona.asignarSexo(genero)
        persona.asignarUbicacion(lugar)
        persona.asignarFechaNacimiento(fecha)
        persona.asignarPadre(datoPadre)
        persona.asignarNacionalidadP(datoNaPa)
        persona.asignarMadre(datoMadre)
        persona.asignarNacionalidadM(datoNaMa)
                     
        listaPersonas.append(persona)
        graba(archivo1,listaPersonas)
        
    def separarCedula(dato):
        """
        Funcionalidad: Se parar los números de la cédula.
        Entradas: La cédula completa.
        Salidas: El primer número de la cédula.
        """
        dato=str(dato)
        dato=dato.split()
        return dato[0]
    
    def regresarMenu(ventana3):
        """
        Funcionalidad: Eliminar la ventana actual y regresar a la del menú principal.
        Entradas: Ventana actual.
        Salidas: Ventana del menú.
        """
        ventana3.destroy()
        menuPrincipal()
        
    def limpiarDatos():
        """
        Funcionalidad: Limpia todos los datos de la ventana de registro.
        Entradas: No hay.
        Salidas: Espacios sin datos.
        """
        entryCita1.delete(0,END)
        entryCita2.delete(0,END)
        entryCita3.delete(0,END)
        entryNombre.delete(0,END)
        entryApellido.delete(0,END)
        opcion.set("M")
        entryDistrito.delete(0,END)
        entryCanton.delete(0,END)
        textEntry.set("Ninguna")
        anno.set("")
        mes.set("")
        dia.set("")
        padre.set("")
        nacioPadre.set("")
        madre.set("")
        nacioMadre.set("")
        
    def datosPadre(event):
        """
        Funcionalidad: Obtener el dato seleccionado en el combobox de Padre.
        Entradas: Evento del combobox.
        Salidas: El dato.
        """
        datoPa=padre.get()
        return datoPa
    
    def nacionalidadP(event):
        """
        Funcionalidad: Obtener el dato seleccionado en el combobox de Nacionalidad Padre.
        Entradas: Evento del combobox.
        Salidas: El dato.
        """
        datoNaPa=nacioPadre.get()
        return datoNaPa
    
    def datosMadre(event):
        """
        Funcionalidad: Obtener el dato seleccionado en el combobox de Madre.
        Entradas: Evento del combobox.
        Salidas: El dato.
        """
        datoMa=madre.get()
        return datoMa
    
    def nacionalidadM(event):
        """
        Funcionalidad: Obtener el dato seleccionado en el combobox de Nacionalidad Madre.
        Entradas: Evento del combobox.
        Salidas: El dato.
        """
        datoNaMa=nacioMadre.get()
        return datoNaMa
    
    def formarListas(listaPersonas):
        """
        Funcionalidad: Formar 2 listas con las personas en la clase separadas por hombres y mujeres.
        Entradas: La lista de personas.
        Salidas: Dos listas, una de hombres y otra de mujeres.
        """
        listaM=[]
        listaH=[]
        for persona in listaPersonas:
            cedula=persona.obtenerCedula()
            nombre=persona.obtenerNombre()
            opcion=cedula+" "+nombre
            if persona.obtenerSexo()=="M":
                listaH.append(opcion)
            else:
                listaM.append(opcion)
        return listaM,listaH

    def tomarMes(event):
        """
        Funcionalidad: Obtener el dato seleccionado en el combobox de mes.
        Entradas: Evento del combobox.
        Salidas: El dato.
        """
        numMes=mes.get()
        return numMes

    def tomarAnno(event):
        """
        Funcionalidad: Obtener el dato seleccionado en el combobox de año.
        Entradas: Evento del combobox.
        Salidas: El dato.
        """
        numAnno=anno.get()
        return numAnno

    def tomarDia(event):
        """
        Funcionalidad: Obtener el dato seleccionado en el combobox de día.
        Entradas: Evento del combobox.
        Salidas: El dato.
        """
        numDia=dia.get()
        return numDia

    def generarProvincia(entryCita1,labelProvincia):
        """
        Funcionalidad: Genera el nombre de la provincia de acuerdo al número de cédula.
        Entradas: La cédula.
        Salidas: El nombre de provincia en el label.
        """
        cedula1=entryCita1.get()
        try:
            if cedula1!="":
                provincia=provinciasDicc[int(cedula1)]
                textEntry.set(provincia)
            else:
                textEntry.set("Ninguna")
        except:
            textEntry.set("Cédula ingresada incorrectamente")
        labelProvincia.after(300,lambda:generarProvincia(entryCita1,labelProvincia))
        return 
                
    def registrarPersona():
        """
        Funcionalidad: Validar cada uno de los datos ingresados y registrar a la persona..
        Entradas: Los datos.
        Salidas: No hay.
        """
        try:
            cedula=entryCita1.get()+entryCita2.get()+entryCita3.get()
            cedula1=entryCita1.get()
            cedula2=entryCita2.get()
            cedula3=entryCita3.get()
            salida=validarCedula(cedula,cedula1,cedula2,cedula3)
            if salida[0]==True:
                if(validarExistencia(salida[1])):
                    nombre=entryNombre.get()
                    if(validarPalabras(nombre)):
                        apellido=entryApellido.get()
                        nombre2=definirNombre(nombre,apellido)
                        if(validarPalabras(apellido)):
                           if(validarLargoApellido(apellido)):
                                genero=opcion.get()
                                distrito=entryDistrito.get()
                                if(validarPalabras2(distrito)):
                                    canton=entryCanton.get()
                                    if(validarPalabras2(canton)):
                                        provincia=entryProvincia.get()
                                        lugar=definirDistritoCanton(distrito,canton,provincia)
                                        if(validarProvincia(provincia)):
                                            numAnno=anno.get()
                                            numMes=mes.get()
                                            numDia=dia.get()
                                            fecha=definirFecha(numAnno,numMes,numDia)
                                            if validarSelectores(numAnno) and validarSelectores(numMes) and validarSelectores(numDia):
                                                if(validarFecha(numAnno,numMes,numDia)):
                                                    datoPa=padre.get()
                                                    datoNaPa=nacioPadre.get()
                                                    datoMa=madre.get()
                                                    datoNaMa=nacioMadre.get()
                                                    if validarSelectores(datoPa) and validarSelectores(datoNaPa) and validarSelectores(datoMa) and validarSelectores(datoNaMa):
                                                       if validarPadres(apellido,datoPa,datoMa):
                                                           datoPadre=separarCedula(datoPa)
                                                           datoMadre=separarCedula(datoMa)
                                                           asignarDatos(salida[1],nombre2,genero,lugar,fecha,datoPadre,datoNaPa,datoMadre,datoNaMa)
                                                           limpiarDatos()
                                                           messagebox.showinfo(message="Datos de usuarios satisfactoriamente registrados.", title="Registro procesado")
        except:
            ""

##################################################################################
            
    #Definición de la ventana 3:
            
    global listaPersonas
    listaPersonas=lee(archivo1)
    ventana3=Tk()
    ventana3.title("Registro de nacimientos")
    ventana3.resizable(False, False)
    window_height = 620
    window_width = 500
    screen_width = ventana3.winfo_screenwidth()
    screen_height = ventana3.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    ventana3.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ventana3.configure(background="white")
    labelTitulo= Label(ventana3, text="Datos de la nueva persona",bg="white",font=("Arial Bold",14,"bold"))
    labelTitulo.place(x=130, y=15)
    labelCita= Label(ventana3, text="Cita:",bg="white",font=("Arial Bold",12,))
    labelCita.place(x=20, y=45)
    entryCita1 = ttk.Entry(ventana3,width=1)
    entryCita1.place(x=175, y=45)
    labelGuion= Label(ventana3, text="-",bg="white",font=("Arial Bold",12,))
    labelGuion.place(x=200, y=45)
    entryCita2 = ttk.Entry(ventana3,width=4)
    entryCita2.place(x=225, y=45)
    labelGuion= Label(ventana3, text="-",bg="white",font=("Arial Bold",12,))
    labelGuion.place(x=265, y=45)
    entryCita3 = ttk.Entry(ventana3,width=4)
    entryCita3.place(x=285, y=45)
    labelNombre= Label(ventana3, text="Nombre:",bg="white",font=("Arial Bold",12,))
    labelNombre.place(x=20, y=80)
    entryNombre = ttk.Entry(ventana3,width=50)
    entryNombre.place(x=175, y=80)
    labelApellido= Label(ventana3, text="Apellidos:",bg="white",font=("Arial Bold",12,))
    labelApellido.place(x=20, y=115)
    entryApellido= ttk.Entry(ventana3,width=50)
    entryApellido.place(x=175, y=115)
    labelSexo= Label(ventana3, text="Sexo:",bg="white",font=("Arial Bold",12,))
    labelSexo.place(x=20, y=150)
    opcion = StringVar()
    opcion.set("M")
    radiobuttonMasculino=Radiobutton(ventana3, text="Masculino", variable=opcion,value="M", bg="white",selectcolor="white")
    radiobuttonMasculino.place(x=175,y=150)
    radiobuttonFemenino=Radiobutton(ventana3, text="Femenino", variable=opcion,value="F", bg="white",selectcolor="white")
    radiobuttonFemenino.place(x=300,y=150)
    labelDistrito= Label(ventana3, text="Distrito:",bg="white",font=("Arial Bold",12,))
    labelDistrito.place(x=20, y=185)
    entryDistrito= ttk.Entry(ventana3,width=50)
    entryDistrito.place(x=175, y=185)
    labelCanton= Label(ventana3, text="Cantón:",bg="white",font=("Arial Bold",12,))
    labelCanton.place(x=20, y=220)
    entryCanton= ttk.Entry(ventana3,width=50)
    entryCanton.place(x=175, y=220)
    labelProvincia= Label(ventana3, text="Provincia:",bg="white",font=("Arial Bold",12,))
    labelProvincia.place(x=20, y=255)
    textEntry = tk.StringVar()
    textEntry.set("Ninguna")
    generarProvincia(entryCita1,labelProvincia)
    entryProvincia= ttk.Entry(ventana3,width=50,state="readonly",textvariable=textEntry)
    entryProvincia.place(x=175, y=255)
    labelDia= Label(ventana3, text="Día:",bg="white",font=("Arial Bold",12,))
    labelDia.place(x=20, y=290)
    labelMes= Label(ventana3, text="Mes:",bg="white",font=("Arial Bold",12,))
    labelMes.place(x=20, y=325)
    labelAnno= Label(ventana3, text="Año:",bg="white",font=("Arial Bold",12,))
    labelAnno.place(x=20, y=360)
    anno=t.Combobox(ventana3,values=numAnnos, state='readonly')
    anno.place(x=175,y=360)
    anno.bind("<<ComboboxSelected>>",tomarAnno)
    mes=t.Combobox(ventana3,values=meses, state='readonly')
    mes.place(x=175,y=325)
    mes.bind("<<ComboboxSelected>>",tomarMes)
    dia=t.Combobox(ventana3,values=dias, state='readonly')
    dia.place(x=175,y=290)
    dia.bind("<<ComboboxSelected>>",tomarDia)
    salida2=formarListas(listaPersonas)
    labelPadre= Label(ventana3, text="Padre:",bg="white",font=("Arial Bold",12,))
    labelPadre.place(x=20, y=395)
    padre=t.Combobox(ventana3,width=47,values=salida2[1], state='readonly')
    padre.place(x=175,y=395)
    padre.bind("<<ComboboxSelected>>",datosPadre)
    labelNacionalidadP= Label(ventana3, text="Nacionalidad padre:",bg="white",font=("Arial Bold",12,))
    labelNacionalidadP.place(x=20, y=430)
    nacioPadre=t.Combobox(ventana3,width=47,values=nacionalidadHombre, state='readonly')
    nacioPadre.place(x=175,y=430)
    nacioPadre.bind("<<ComboboxSelected>>",nacionalidadP)
    labelMadre= Label(ventana3, text="Madre:",bg="white",font=("Arial Bold",12,))
    labelMadre.place(x=20, y=465)
    madre=t.Combobox(ventana3,width=47,values=salida2[0], state='readonly')
    madre.place(x=175,y=465)
    madre.bind("<<ComboboxSelected>>",datosMadre)
    labelNacionalidadM= Label(ventana3, text="Nacionalidad madre:",bg="white",font=("Arial Bold",12,))
    labelNacionalidadM.place(x=20, y=500)
    nacioMadre=t.Combobox(ventana3,width=47,values=nacionalidadMujer, state='readonly')
    nacioMadre.place(x=175,y=500)
    nacioMadre.bind("<<ComboboxSelected>>",nacionalidadM)
    #Botones
    botonRegistro=Button(ventana3, text="Registrar", command=registrarPersona, height=2, width=10,font=("Arial Bold",12))
    botonRegistro.place(x=85, y=545)
    botonLimpiar=Button(ventana3, text="Limpiar", command=limpiarDatos,height=2, width=10,font=("Arial Bold",12))
    botonLimpiar.place(x=200, y=545)
    botonRegresar=Button(ventana3, text="Regresar", command=lambda:regresarMenu(ventana3),height=2, width=10,font=("Arial Bold",12))
    botonRegresar.place(x=315, y=545)

##################################################################################
    
#Generar ventana del menú principal:
    
def menuPrincipal():
    """
    Funcionalidad: Generar el menú principal.
    Entradas: Ninguna.
    Salidas: El menú generado.
    """

##################################################################################

    #Funciones generales de la ventana2:
    
    def salirVentana2():
        """
        Funcionalidad: Eliminar la ventana actual.
        Entradas: Ventana actual.
        Salidas: No hay.
        """
        graba(archivo1,listaPersonas)
        ventana2.destroy()
        
##################################################################################
        
    #Definicion de la ventana 2:

    global listaPersonas
    listaPersonas=lee(archivo1) 
    ventana2=Tk()
    ventana2.title("TSE")
    ventana2.geometry("400x250")
    window_height = 250
    window_width = 400
    screen_width = ventana2.winfo_screenwidth()
    screen_height = ventana2.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    ventana2.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    titulo=Label(ventana2,text="Tribunal Supremo de Elecciones", font=("Arial Bold",14))
    titulo.place(x=80, y=1)
    totalPers=Label(ventana2,text="Total de personas: "+str(len(listaPersonas)), font=("Arial Bold",10))
    totalPers.place(x=260, y=30)
    registro=Button(ventana2, text="Registrar Nacimiento", command=lambda:registroNacimientos(ventana2), font=("Arial Bold",12))
    registro.place(x=120, y=70)
    arbol=Button(ventana2, text="Mostrar Árbol Genealógico", command=lambda: generarVentana4(ventana2), font=("Arial Bold",12))
    arbol.place(x=100, y=110)
    certi=Button(ventana2, text="Certificado de Nacimiento", command=lambda: generarVentana5(ventana2),font=("Arial Bold",12))
    certi.place(x=103, y=150)
    salir=Button(ventana2, text="Salir",command=salirVentana2, font=("Arial Bold",12))
    salir.place(x=170, y=190)
    ventana2.mainloop()
    
def registroNacimientos(ventana2):
    """
    Funcionalidad: Generar la ventana.
    Entradas: La ventana2 (el menú principal).
    Salidas: Ninguna.
    """
    ventana2.destroy()
    #Llamada a la generación de la ventana:
    generarVentana3()

##################################################################################
    
#Funciones generales del programa:
    
def formarMatriz(datos):
    """
    Funcionalidad: Forma la matriz según los datos de los funcionarios del Registro Civil.
    Entradas: Los datos de los funcionarios del Registro Civil.
    Salidas: La matriz generada con los de los funcionarios del Registro Civil.
    """
    listaFuncionarios2=[]
    if(validarCantidad(datos)):
        personas=datos.split("|")
        for persona in personas:
            dato=persona.split("#")
            listaFuncionarios2.append(dato)
    else:
        dato=datos.split("#")
        listaFuncionarios2.append(dato)
    return listaFuncionarios2

def limpiar():
    """
    Funcionalidad: Limpiar los datos de la ventana de ingreso.
    Entradas: No hay.
    Salidas: Espacios de texto sin datos.
    """
    entryUsuario.delete(0,END)
    entryContrasenna.delete(0,END)

def ingresar():
    """
    Funcionalidad: Validar que los datos de ingreso estén bien.
    Entradas: Correo y contraseña.
    Salidas: Mensaje de error o dirige al menú principal.
    """
    usuario=entryUsuario.get()
    contrasenna=entryContrasenna.get()
    if(validarCorreo(usuario)):
        if(validarContrasenna(contrasenna)):
            listaFuncionarios2=formarMatriz(listaDeFuncionarios[0])
            if(validarFuncionarios(listaFuncionarios2,usuario,contrasenna)):
                ventana1.destroy()
                menuPrincipal()
                 
            else:
                 messagebox.showinfo(message="Los datos ingresados no existen en la base de datos. Verífiquelos.", title="Error")   
        else:
             messagebox.showinfo(message="Datos de la contraseña ingresados incorrectamente.", title="Error")   
           
    else:
         messagebox.showinfo(message="Datos de usuario ingresados incorrectamente.", title="Error")

##################################################################################        
    
#Definición de la ventana1:
        
ventana1=Tk()
ventana1.title("Registro de funcionarios")
ventana1.resizable(False, False)
window_height = 150
window_width = 400
screen_width = ventana1.winfo_screenwidth()
screen_height = ventana1.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
ventana1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
ventana1.configure(background="white")
labelUsuario= Label(ventana1, text="Usuario:",bg="white")
labelUsuario.place(x=10, y=25)
entryUsuario = ttk.Entry(ventana1,width=45)
entryUsuario.place(x=100, y=25)
labelContrasenna= Label(ventana1, text="Contraseña:",bg="white")
labelContrasenna.place(x=10, y=55)
entryContrasenna = ttk.Entry(ventana1, show="*",width=45)
entryContrasenna.place(x=100, y=55)
botonIngreso=Button(ventana1, text="Ingresar", height=2, width=10,command=ingresar)
botonIngreso.place(x=110, y=90)
botonLimpio=Button(ventana1, text="Limpiar", height=2, width=10, command=limpiar)
botonLimpio.place(x=220, y=90)

##################################################################################

#Variables globales de lectura:

listaDeFuncionarios=leer(archivo)
listaPersonas=lee(archivo1)
for personas in listaPersonas:
    salida=personas.obtenerTodo()
    print(salida[0],salida[1],salida[2],salida[3],salida[4],salida[5],salida[6],salida[7],salida[8])
