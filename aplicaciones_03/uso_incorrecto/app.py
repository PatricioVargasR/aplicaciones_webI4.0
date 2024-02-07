"""
Aplicación basada en el patrón de diseño MVC sin utilizar
prácticas recomendadas
"""

import web  # Importamos el módulo

# Definimos las direcciones de nuestro sitio
urls = ("/", "Index", "/pagina_saludo", "Saludo", "/pagina_despedida", "Despedida")


# Creamos la aplicación utilizando las URLS y las clases
app = web.application(urls, globals())


# Definimos las funcióones correspondientes
class Index:
    def GET(self):
        return "Bienvenido a la página principal"


class Saludo:
    def GET(self):
        return "Hola usuario, discubriste la primera página"


class Despedida:
    def GET(self):
        return "Haz hackeado a la NASA, congratulations"


if __name__ == "__main__":
    app.run()
