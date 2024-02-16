import web

# Creamos las rutas y sus respectivos controladores
urls = (
    "/", "mvc.controllers.calculadora.Calculadora"
)

# Cremaos la aplicación con las rutas y las clases
app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()