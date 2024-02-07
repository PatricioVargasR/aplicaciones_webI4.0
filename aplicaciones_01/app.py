# Importamos el módulo correspondiente
import web

# Definimos las URLs de nuestro sitio
urls = (
    "/", "hello",
    "/pagina2", "Pagina2",
)

# Creamos la aplicación utilizando las URLs que declaramos anteriormente
# Buscamos las clases en nuestro archivo utilizando globals
app = web.application(urls, globals())

# Hola

# Definimos una clase con el nombre igual al que definimos en la URL
class hello:
    # Definimos una función que recibe name como parámetro
    def GET(self):
        return "Hello página 1!"


class Pagina2:
    def GET(self):
        return 'Hola página2'

# Verificamos que el script se esté ejectuando directamente
if __name__ == "__main__":
    # Iniciamos la aplicación
    app.run()
