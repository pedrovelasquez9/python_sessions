import subprocess

#subprocess
subprocess.run(['ls'])
resultado = subprocess.run(['python', '--version'], capture_output=True, encoding='UTF-8')
subprocess.run(['touch', 'text_file.txt'])
print(resultado)

#agregando inputs
saludo = print("Hola mundo")
subprocess.run(['python'], input=saludo)