#forzar argumentos con nombre
def holaNombre(*, nombre, edad):
    print(nombre, edad)

holaNombre(edad=30, nombre="Pedro")

#argumentos en diccionario
diccionario_de_params = {"edad": 50, "nombre":"Pedro J."}
holaNombre(**diccionario_de_params)

#decoradores
def print_argument(func):
    def wrapper(the_number):
        print("Argument for", func.__name__, "is", the_number)
        new_number = the_number * 2
        return func(new_number)
    return wrapper

@print_argument
def add_one(x):
    return x + 1

print(add_one(1))

#funciones anonimas o lambda functions
una_variable = lambda x: x+1
print(una_variable(1))

numeros = [1, 2, 3]
dobles = map(lambda x: x*2, numeros)
mi_lista = list(dobles)
print(mi_lista)