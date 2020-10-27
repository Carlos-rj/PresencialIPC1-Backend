from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from historial import Historial

Operaciones = []

app = Flask(__name__)
CORS(app)

#ENDPOINT - RUTA
@app.route('/', methods=['GET'])
def rutaInicial():
    return("<h1> EXPLICACION PRACTICA PRESENCIAL </h1>")

#RUTA 1 - SUMA
@app.route('/Suma', methods=['POST'])
def suma():
    global Operaciones
    try:
        n1 = float(request.json['a'])
        n2 = float(request.json['b'])
        resultado = n1 + n2
        Operacion = Historial(n1,n2,"Suma",resultado)
        Operaciones.append(Operacion)    
        return(jsonify({'message': "Exito", 'result': resultado}))
    except:
        return(jsonify({'message': "Error", 'result': 0}))

#RUTA 2 - RESTA
@app.route('/Resta', methods=['POST'])
def resta():
    global Operaciones
    try:
        n1 = float(request.json['a'])
        n2 = float(request.json['b'])
        resultado = n1 - n2
        Operacion = Historial(n1,n2,"Resta",resultado)
        Operaciones.append(Operacion)    
        return(jsonify({'message': "Exito", 'result': resultado}))
    except:
        return(jsonify({'message': "Error", 'result': 0}))

@app.route('/Division', methods=['POST'])
def division():
    global Operaciones
    try:
        n1 = float(request.json['a'])
        n2 = float(request.json['b'])
        resultado = n1 / n2
        Operacion = Historial(n1,n2,"Division",resultado)
        Operaciones.append(Operacion)    
        return(jsonify({'message': "Exito", 'result': resultado}))
    except:
        return(jsonify({'message': "Error", 'result': 0}))

@app.route('/Multiplicacion', methods=['POST'])
def multiplicacion():
    global Operaciones
    try:
        n1 = float(request.json['a'])
        n2 = float(request.json['b'])
        resultado = n1 * n2
        Operacion = Historial(n1,n2,"Multiplicacion",resultado)
        Operaciones.append(Operacion)    
        return(jsonify({'message': "Exito", 'result': resultado}))
    except:
        return(jsonify({'message': "Error", 'result': 0}))

@app.route('/Potencia', methods=['POST'])
def potencia():
    global Operaciones
    try:
        n1 = float(request.json['a'])
        n2 = float(request.json['b'])
        resultado = n1 ** n2
        Operacion = Historial(n1,n2,"Potencia",resultado)
        Operaciones.append(Operacion)    
        return(jsonify({'message': "Exito", 'result': resultado}))
    except:
        return(jsonify({'message': "Error", 'result': 0}))

@app.route('/Raiz', methods=['POST'])
def raiz():
    global Operaciones
    try:
        n1 = float(request.json['a'])
        n2 = float(request.json['b'])
        resultado = n1 ** (1/n2)
        Operacion = Historial(n1,n2,"Raiz",resultado)
        Operaciones.append(Operacion)    
        return(jsonify({'message': "Exito", 'result': resultado}))
    except:
        return(jsonify({'message': "Error", 'result': 0}))

@app.route('/Historial', methods = ['GET'])
def historial():
    global Operaciones
    Datos = []
    for op in Operaciones:
        dato = {
            'fecha': op.getFecha(),
            'numero1': op.getA(),
            'numero2': op.getB(),
            'operacion': op.getOpereacion(),
            'resultado': op.getResultado()
        }
        Datos.append(dato)
    return(jsonify(Datos))


if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=5000, debug=True)