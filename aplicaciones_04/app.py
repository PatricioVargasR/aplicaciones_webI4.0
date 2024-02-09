# Importamos el módulo correspondiente
import web



# Definimos las URLs de nuestro sitio
urls = (
    "/", "mvc.controllers.index.Index",
    "/contactos", "mvc.controllers.contactos.Contactos",
    "/productos", "mvc.controllers.productos.Productos",
    "/python", "mvc.controllers.python.Python"
)

# Creamos la aplicación utilizando las URLs que declaramos anteriormente
# Buscamos las clases en nuestro archivo utilizando globals
app = web.application(urls, globals())


# Verificamos que el script se esté ejectuando directamente
if __name__ == "__main__":
    # Iniciamos la aplicación
    app.run()
