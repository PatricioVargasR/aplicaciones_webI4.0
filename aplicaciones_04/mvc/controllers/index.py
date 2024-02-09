import web

# Buscamos las templates de HTML con una ruta
render = web.template.render('mvc/views/')

class Index:
    def GET (self):
        return render.index()