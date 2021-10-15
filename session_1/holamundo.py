#esto es un comentario
import random
def saludo(nombre=''):
    if nombre == '':
        print('ingresa un nombre')
    else:
        print("hola ...")
        for letra in nombre:
            print(letra)

saludo()
saludo('Pedro')

#random int
aleatorio = random.randint(1,100)
if isinstance(aleatorio, int):
    print(aleatorio)

#diccionarios
mi_diccionario = {"nombre": "Pedro", "apellido": "Plasencia"}
mi_diccionario2 = {"edad":30, "dev":True}
mi_diccionario3 = mi_diccionario | mi_diccionario2
print(mi_diccionario["nombre"])
print(mi_diccionario.get("apellido"))
print(mi_diccionario.get("edad"))
print(mi_diccionario3 == mi_diccionario2)
print(mi_diccionario.keys())

for key, val in mi_diccionario3.items():
    print(key + ":" + str(val))