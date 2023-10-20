from flask import Flask, jsonify
from flask_cors import CORS
from Pelicula_DAO import Pelicula_DAO
from flask.globals import request

pelicula_handler = Pelicula_DAO()
app = Flask(__name__)
CORS(app)

pelicula_handler.agregar_peli("1","Batman","Acción")
pelicula_handler.agregar_peli("2","Iron Man","Acción")
pelicula_handler.agregar_peli("3","El Conjuro","Terror")
pelicula_handler.agregar_peli("4","Son como niños","Comedia")
pelicula_handler.agregar_peli("5","Saw","Terror")


@app.route("/")
def index():
  return "<h1> Bienvenido al  backend! de la Práctica3 </h1>"

@app.route("/nueva-pelicula",methods=['POST'])
def agregar_peli():
  response={}
  id = request.json["id"]
  nombre=request.json["nombre"]
  genero=request.json["genero"]
  if(pelicula_handler.agregar_peli(id,nombre,genero)):
    response={
      "estado":"Correcto",
      "mensaje":"Película agregada exitosamente!"
    }
    return response
  else:
    response={
      "estado":"Error",
      "mensaje":"La película ya existe!"
    }
    return response

@app.route("/pelicula-por-genero/<genero>",methods=['GET'])

def genero_peli(genero):
  return pelicula_handler.genero_peli(genero)

@app.route("/actualizar-pelicula/<nombre>",methods=['PUT'])

def actualizar_peli(nombre):
    return pelicula_handler.actualizar_peli(nombre)
 
   

if __name__ == "__main__":
    app.run(threaded = True, port=5000, debug=True)
