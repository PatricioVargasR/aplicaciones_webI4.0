import web

# Creamos una variable que carga con todas las plantillas
render = web.template.render("mvc/views/")

# Clase que se encarga de realizar el proceso de la vista
class Calculadora:

    # Función GET de la página
    def GET(self):
        try:
            # Inicializamos variables
            numero_1= 0
            numero_2 = 0
            suma = 0
            # Cargamos la vista enviando las variables como parametros
            return render.calculadora(numero_1, numero_2, suma)
        except Exception as error:
            return f'Ocurrió un error {error}'

    # Función POST de la página
    def POST(self):
        try:
            # Obtenemos los valores de los inputs que se hayan enviado
            form = web.input()
            # Sumamos ambas entradas
            suma = float(form.numero_1) + float(form.numero_2)
            # Cargamos la vista ahora con los valores ingresados en el formulario y el resultado
            return render.calculadora(form.numero_1, form.numero_2, suma)
        except Exception as error:
            return f'Ocurrió un error {error}'