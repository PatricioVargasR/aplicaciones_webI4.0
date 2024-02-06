# Definimos una clase con el nombre igual al que definimos en la URL
class hello2:
    # Definimos una función que recibe name como parámetro
    def GET(self, name):
        # Verifica que el nombre no exista, en caso de ser así, asigna un valor
        if not name:
            name = "World"
        return "Hello " + name + " soy un clon!"
