class Pelicula:

    def __init__(self, id,nombre,genero):
        self.id = id
        self.nombre = nombre
        self.genero = genero
    
    def dump(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero
        }


