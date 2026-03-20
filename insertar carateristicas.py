import sqlite3

conexion = sqlite3.connect("la_velada.db")
cursor = conexion.cursor()

class Insertar_Caracteristicas:
    def __init__(self, id_caracteristicas, id_participante, nombre, peso, Altura, Estilo):
        self.id_caracteristicas = id_caracteristicas
        self.id_participante = id_participante
        self.nombre = nombre
        self.peso = peso
        self.Altura = Altura
        self.Estilo = Estilo

    def insertar_datos(self):
        cursor.execute("INSERT INTO caracteristicas (id_caracteristicas, id_participante, nombre, peso, altura, estilo) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.id_caracteristicas, self.id_participante, self.nombre, self.peso, self.Altura, self.Estilo))
        print("Datos insertados correctamente.")

conexion.commit()
conexion.close()