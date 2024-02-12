# Importamos el módulo correspondiente
import web

# Definimos nuestras URLS
urls = (
    '/', 'mvc.controllers.datos_personales.Datos',
    '/contactos', 'mvc.controllers.contactos.Contactos'
)

# Creamos la aplicación
app = web.application(urls, globals())

# Le decimos que ejecute este script como el "padre"
if __name__ == '__main__':
    app.run()