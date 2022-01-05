##################################################################################
#Elaborado por Mónica Alfaro P y Jennifer Alvarado B
#Inicio: 28/07/2020 17:00
#Última modificación: 03/08/2020 19:00
#Versión 3.8.2
##################################################################################

#Importación de librerías:
import re

##################################################################################

#Validaciones:

def validarFuncionarios(listaFuncionarios2,usuario,contrasenna):
    """
    Funcionalidad: Valida que los datos ingresados correspondan a un usuario permitido.
    Entradas: Datos ingresados y lista de funcionarios.
    Salidas: True (está registrado) o False (no está registrado).
    """
    for datos in listaFuncionarios2:
        if datos[0]==usuario and datos[1]==contrasenna:
            return True
    return False
    
def validarCantidad(string):
    """
    Funcionalidad: Valida si son los datos de una o más personas.
    Entradas: El string ingresado por el usuario.
    Salidas: True (es correcto) o False (es incorrecto).
    """
    if "|" in string:
        return True
    else:
        return False
        
def validarCorreo(correo):
    """
    Funcionalidad: Validar que el formato del correo sea correcto.
    Entradas: El correo.
    Salidas: True (es correcto) o False (es incorrecto).
    """
    if re.match(r'(^[\w_.-]+)@([\w]+)([\w]+).([\w]+)$',correo):
        return True
    else:
        return False

def validarContrasenna(contrasenna):
    """
    Funcionalidad: Validar que la contraseña cumpla con los requisitos.
    Entradas: La contraseña.
    Salidas: True (es correcta) o False (es incorrecta).
    """
    if re.search('[a-zA-Z]',contrasenna):
        if(re.search('\d',contrasenna)):
            if(5<=len(contrasenna)<=15):
                return True
    return False
