from Pelicula import Pelicula
import json

class Pelicula_DAO:

    def __init__(self):
        self.peliculas=[]
        self.id_contador = 1


    
    def agregar_peli(self, id,nombre, genero):
        for pelicula in self.peliculas:
            if pelicula.nombre == nombre:
                return False
        new = Pelicula(id, nombre, genero)
        self.peliculas.append(new)
        self.id_contador += 1
        print("Pelicula Agregada con éxito!")
        return True
    

    def genero_peli(self, genero):
        return json.dumps([Pelicula.dump() for Pelicula in self.peliculas if Pelicula.genero == genero], indent=4)
    
    def actualizar_peli(self,nombre):
        return json.dumps([Pelicula.dump() for Pelicula in self.peliculas if Pelicula.nombre == nombre], indent=4)
       