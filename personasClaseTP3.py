##################################################################################
#Elaborado por Mónica Alfaro P y Jennifer Alvarado B
#Inicio: 27/07/2020 15:00
#Última modificación: 03/08/2020 17:45
#Versión 3.8.2
##################################################################################

class Persona:
    def __init__(atri):
        atri.cedula=""
        atri.nombre=""
        atri.sexo=""
        atri.ubicacion=""
        atri.fechaNacimiento=""
        atri.padre=""
        atri.nacionalidadP=""
        atri.madre=""
        atri.nacionalidadM=""
        
    def asignarCedula(atri,pcedula):
        """
        Funcionalidad: Asigna la cédula ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.cedula=pcedula

    def asignarNombre(atri,pnombre):
        """
        Funcionalidad: Asigna el nombre ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.nombre=pnombre
        
    def asignarSexo(atri,psexo):
        """
        Funcionalidad: Asigna el sexo ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.sexo=psexo
        
    def asignarUbicacion(atri,pubicacion):
        """
        Funcionalidad: Asigna la ubicación ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.ubicacion=pubicacion
        
    def asignarFechaNacimiento(atri,pfechaNacimiento):
        """
        Funcionalidad: Asigna la fecha de nacimiento ingresada al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.fechaNacimiento=pfechaNacimiento

    def asignarPadre(atri,ppadre):
        """
        Funcionalidad: Asigna el padre ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.padre=ppadre
        
    def asignarNacionalidadP(atri,pnacionalidadP):
        """
        Funcionalidad: Asigna la nacionalidad del padre ingresado al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.nacionalidadP=pnacionalidadP
        
    def asignarMadre(atri,pmadre):
        """
        Funcionalidad: Asigna la madre ingresada al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.madre=pmadre
        
    def asignarNacionalidadM(atri,pnacionalidadM):
        """
        Funcionalidad: Asigna la nacionalidad de la madre ingresada al atributo.
        Entradas: Dato ingresado.
        Salidas: El atributo con el dato.
        """
        atri.nacionalidadM=pnacionalidadM

    def obtenerCedula(atri):
        """
        Funcionalidad: Obtiene la cedula del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.cedula

    def obtenerNombre(atri):
        """
        Funcionalidad: Obtiene el nombre del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.nombre

    def obtenerSexo(atri):
        """
        Funcionalidad: Obtiene el sexo del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.sexo

    def obtenerUbicacion(atri):
        """
        Funcionalidad: Obtiene la ubicación del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.ubicacion

    def obtenerFechaNacimiento(atri):
        """
        Funcionalidad: Obtiene la fecha de nacimiento del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.fechaNacimiento

    def obtenerPadre(atri):
        """
        Funcionalidad: Obtiene el padre del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.padre

    def obtenerNacionalidadP(atri):
        """
        Funcionalidad: Obtiene la nacionalidad del padre del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.nacionalidadP

    def obtenerMadre(atri):
        """
        Funcionalidad: Obtiene la madre del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.madre

    def obtenerNacionalidadP(atri):
        """
        Funcionalidad: Obtiene la nacionalidad de la madre del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.nacionalidadM

    def obtenerTodo(atri):
        """
        Funcionalidad: Obtiene todo del atributo.
        Entradas: El atributo.
        Salidas: El dato.
        """
        return atri.cedula, atri.nombre, atri.sexo, atri.ubicacion, atri.fechaNacimiento, atri.padre, atri.nacionalidadP,atri.madre,atri.nacionalidadM
    


    
  
            
