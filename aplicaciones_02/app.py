# Importamos el módulo correspondiente
import web

# Definimos las URLs de nuestro sitio
urls = (
    "/", "mvc.controllers.hello.hello",
    "/", "mvc.controllers.hello2.hello2")

# Creamos la aplicación utilizando las URLs que declaramos anteriormente
# Buscamos las clases en nuestro archivo utilizando globals
app = web.application(urls, globals())



# Verificamos que el script se esté ejectuando directamente
if __name__ == "__main__":
    # Iniciamos la aplicación
    app.run()
