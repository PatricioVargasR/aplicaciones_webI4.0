# Importamos el módulo correspondiente
import web

# Definimos las URLs de nuestro sitio
urls = ("/(.*)", "hello")

# Creamos la aplicación utilizando las URLs que declaramos anteriormente
# Buscamos las clases en nuestro archivo utilizando globals
app = web.application(urls, globals())


# Definimos una clase con el nombre igual al que definimos en la URL
class hello:
    # Definimos una función que recibe name como parámetro
    def GET(self, name):
        # Verifica que el nombre no exista, en caso de ser así, asigna un valor
        if not name:
            name = "World"
        return "Hello " + name + "!"


# Verificamos que el script se esté ejectuando directamente
if __name__ == "__main__":
    # Iniciamos la aplicación
    app.run()
