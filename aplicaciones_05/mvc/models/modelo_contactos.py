"""
    Archivo que almacena el módelo de los contactos
"""


# Creamos eel modelo de los contactos
# Se optó guardar datos como variable de instancia por la posibilidad de poder ser utilizados en otros
# métodos de la clase
class ModeloContactos:

    # Función de inicio de la clase
    def __init__(self):
        self.datos = [
            {
                "nombre": "Juan",
                "correo": "dejah@gmail.com"
            },
            {
                "nombre": "Jonh",
                "correo": "jonh@gmail.com"
            }
        ]

    # Función que obtiene todos los contactos
    def obtenerContactos(self):
        return self.datos
