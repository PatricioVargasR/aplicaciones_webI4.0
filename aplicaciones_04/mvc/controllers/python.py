import web
from mvc.models.m_index import ModelIndex  # Importamos la clase ModelIndex de la ruta específicada

render = web.template.render('mvc/views/')

m_index = ModelIndex()

class Python:
    def GET(self):
        return render.python(m_index.nombre)