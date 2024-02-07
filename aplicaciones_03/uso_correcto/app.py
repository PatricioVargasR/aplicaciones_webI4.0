"""
Aplicación basada en el patrón de diseño MVC utilizando
buenas prácticas o prácticas recomendadas
"""

import web  # Importamos el módulo

# Definimos las direcciones de nuestro sitio
urls = (
    "/",
    "mvc.controllers.index.Index",
    "/pagina_saludo",
    "mvc.controllers.saludo.Saludo",
    "/pagina_despedida",
    "mvc.controllers.despedida.Despedida",
)

# Creamos la aplicación utilizando las URLS y las clases
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
