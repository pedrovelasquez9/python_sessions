class Vehicle:
    def __init__(self, speed = 0, started=False):
        self.speed = speed
        self.started = started

    def start(self):
        self.started = True
        print("Genial, el coche está encendido")
 
    def increase_speed(self):
        if self.started:
            self.speed
            print('Vrooooom!', self.speed)
        else:
            print("El coche está apagado, enciéndelo antes de acelerar")
 
    def stop(self):
        self.speed = 0
        print('Coche detenido')

class Coche(Vehicle):
    capo_abierto = False
    def abrir_capo(self):
        self.capo_abierto = True
        print("el capo está abierto")
    def cerrar_capo(self):
        self.capo_abierto = False

class Motocicleta(Vehicle):
    def __init__(self, es_motocicleta=True):
        self.es_motocicleta = es_motocicleta
        super().__init__()
