import sqlite3

conexion = sqlite3.connect("la_velada.db")
cursor = conexion.cursor()

class Partcipantes :
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

class Caracteristicas:
    def __init__(self, id_caracteristicas, id_participante, nombre, peso, Altura, Estilo):
        self.id_caracteristicas = id_caracteristicas
        self.id_participante = id_participante
        self.nombre = nombre
        self.peso = peso
        self.Altura = Altura
        self.Estilo = Estilo

    def insertar_datos(self):
        cursor.execute("INSERT INTO Caracteristicas (id_caracteristicas, id_participantes, nombre, peso, altura, estilo) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.id_caracteristicas, self.id_participante, self.nombre, self.peso, self.Altura, self.Estilo))
        conexion.commit()
        print("Datos insertados correctamente.")

class combates:
    def __init__(self, id_combate, id_participante1, id_participante2, Nombres,nombre2,Tipo_de_combate):
        self.id_combate = id_combate
        self.id_participante1 = id_participante1
        self.id_participante2 = id_participante2
        self.Nombres = Nombres
        self.nombre2 = nombre2
        self.Tipo_de_combate = Tipo_de_combate
        

    def insertar_datos(self):
        cursor.execute("INSERT INTO Combates (id_combate, id_participante1, id_participante2, Nombres, nombre2, Tipo_de_combate) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.id_combate, self.id_participante1, self.id_participante2, self.Nombres, self.nombre2, self.Tipo_de_combate))
        conexion.commit()
        print("Datos insertados correctamente.")



conexion.close()

