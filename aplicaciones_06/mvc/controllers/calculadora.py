import web


render = web.template.render("mvc/views/")


class Calculadora:

    def GET(self):
        try:
            numero_1= 0
            numero_2 = 0
            suma = 0
            return render.calculadora(numero_1, numero_2, suma)
        except Exception as error:
            return f'Ocurrió un error {error}'

    def POST(self):
        try:
            form = web.input()
            suma = float(form.numero_1) + float(form.numero_2)
            return render.calculadora(form.numero_1, form.numero_2, suma)
        except Exception as error:
            return f'Ocurrió un error {error}'