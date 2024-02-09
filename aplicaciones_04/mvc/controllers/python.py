import web
from mvc.models.m_index import ModelIndex  # Importamos la clase ModelIndex de la ruta específicada

render = web.template.render('mvc/views/')

m_index = ModelIndex()

class Python:
    def GET(self):
        try:
            productos = m_index.consultarProductos()
            return render.python(productos)
        except Exception as e:
            print(f"Error 101 -index {e.args}")
            return "Ups algo salió mal"