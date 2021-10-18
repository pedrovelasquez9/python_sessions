import json

mi_json = '{"nombre":"Pedro", "apellido":"Plasencia", "programa": true}'
data_from_string = json.loads(mi_json)
print(type(data_from_string))
#podemos hacer lo inverso con dumps
print(type(json.dumps(data_from_string)))

with open("archivo.json", "w") as json_file:
    json.dump(data_from_string, json_file)

with open("archivo.json") as mi_json:
    objeto = json.load(mi_json)
    print(objeto)