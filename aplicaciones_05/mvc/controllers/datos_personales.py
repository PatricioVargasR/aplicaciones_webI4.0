"""
    Archivo el cuál se encargará de manejar las operaciones sobre los datos
"""
import web  # Importamos el módulo
from ..models.modelo_datosPersonales import ModeloDatosPersonales  # Importamos la clase correspondiente del módelo

DATOS_PERSONALES = ModeloDatosPersonales()  # Creamos una objeto de la clase ModeloContactos()

render = web.template.render('mvc/views/', base='layout_index')  # Obtenemos la ruta donde se renderiza las plantillas
# Agregamos ,base='layout' para utilizar una plantilla base


# Creamos una clase llamada Contactos
class Datos:
    # Función que obtendrá todos los contacots
    def GET(self):
        try:
            datos_personales = DATOS_PERSONALES.obtenerDatosPersonales()

            return render.index(datos_personales)
        except Exception as e:
            print(f"Error 102 - Datos Personales {e.args}")

            return "Ocurrió algún error"
