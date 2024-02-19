# Creamos la clase
class ModeloCalculadora:
    # Generamos una función la cuál recibe dos parámetros y devuelve un flotante
    def sumar(self, numero_1: str, numero_2: str) -> float:
        try:
            # Realiza la operación correspondiente
            resultado = float(numero_1) + float(numero_2)
            # Regresa el reusltado
            return resultado
        # En caso de haber un error
        except Exception as e:
            # Imprime el error y retorna un valor
            print(f'Ocurrió un error {e}')
            return 0.0