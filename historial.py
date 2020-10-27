from datetime import date
from datetime import datetime
class Historial:
    def __init__(self,a,b,operacion,resultado):
        now = datetime.now()
        format = now.strftime('%d/%m/%Y - %H:%M:%S')
        self.fecha = format
        self.a = a
        self.b = b
        self.operacion = operacion
        self.resultado = resultado
    
    def getFecha(self):
        return self.fecha

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getOpereacion(self):
        return self.operacion

    def getResultado(self):
        return self.resultado
    