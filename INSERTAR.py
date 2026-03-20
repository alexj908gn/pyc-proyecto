import sqlite3

conexion = sqlite3.connect("la_velada.db")
cursor = conexion.cursor()

class Insertar_Partcipantes :
    def __init__(self, id_participante, id_caracteristica, nombre, canal_de_internet):
        self.id_participante = id_participante
        self.id_caracteristica = id_caracteristica
        self.nombre = nombre
        self.canal_de_internet = canal_de_internet


    def insertar_datos(self):
        cursor.execute("INSERT INTO participantes (id_ participantes,id_caracteristicas,nombre, canal_de_internet) VALUES (?, ?, ?, ?)",
                       (self.id_participante, self.id_caracteristica, self.nombre, self.canal_de_internet))
        conexion.commit()
        print("Datos insertados correctamente.")

        
conexion.close()