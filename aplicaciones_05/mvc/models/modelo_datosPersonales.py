"""
    Archivo que almacena el módelo de los contactos
"""


# Creamos eel modelo de los contactos
# Se optó guardar datos como variable de instancia por la posibilidad de poder ser utilizados en otros
# métodos de la clase
class ModeloDatosPersonales:

    # Función de inicio de la clase
    def __init__(self):
        self.datos = ['Patricio de Jesús', '19 años', 'Tulancingo de Bravo', 'México']

    # Función que obtiene todos los contactos
    def obtenerDatosPersonales(self):
        return self.datos
