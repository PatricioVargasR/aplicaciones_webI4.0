"""
    Archivo el cuál se encargará de manejar las operaciones sobre los datos
"""
import web  # Importamos el módulo
from ..models.modelo_contactos import ModeloContactos  # Importamos la clase correspondiente del módelo

CONTACTOS = ModeloContactos()  # Creamos una objeto de la clase ModeloContactos()

render = web.template.render('mvc/views/')  # Obtenemos la ruta donde se renderiza las plantiallas


# Creamos una clase llamada Contactos
class Contactos:
    # Función que obtendrá todos los contacots
    def GET(self):
        try:
            contactos = CONTACTOS.obtenerContactos()

            return render.contactos(contactos)
        except Exception as e:
            print(f"Error 101 - Contactos {e.args}")

            return "Ocurrió algún error"
