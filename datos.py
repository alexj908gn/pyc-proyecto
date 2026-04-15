import sqlite3

conexion = sqlite3.connect("la_velada.db")
cursor = conexion.cursor()

class Participantes :
    def __init__(self, id_participante, id_caracteristica, nombre, canal_de_internet):
        self.id_participante = id_participante
        self.id_caracteristica = id_caracteristica
        self.nombre = nombre
        self.canal_de_internet = canal_de_internet


    def insertar_participantes(self):
        cursor.execute("INSERT INTO participantes (id_ participantes,id_caracteristicas,nombre, canal_de_internet) VALUES (?, ?, ?, ?)",
                       (self.id_participante, self.id_caracteristica, self.nombre, self.canal_de_internet))
        conexion.commit()
        print("Datos insertados correctamente.")
    def actualizar_participantes(self,nombre, canal_de_internet):
        cursor.execute("UPDATE Participantes SET Nombre = ? and SET Canal_de_internet = ? WHERE id_participantes = ?", (nombre, canal_de_internet, self.id_participante))
        conexion.commit()
        print("Datos actualizados correctamente.")
    def eliminar_de_participantes(self):
        cursor.execute("DELETE FROM Participantes WHERE id_participantes = ?", (self.id_participante,))
        conexion.commit()
        print("Datos eliminados correctamente.")
    def consultar_participantes(self,fila,resultado):
        cursor.execute("SELECT * FROM Participantes WHERE id_participantes = ?", (self.id_participante,))
        resultado = cursor.fetchall()
        for fila in resultado:
             print(fila)
        
class Caracteristicas:
    def __init__(self, id_caracteristicas, id_participante, nombre, peso, Altura, Estilo):
        self.id_caracteristicas = id_caracteristicas
        self.id_participante = id_participante
        self.nombre = nombre
        self.peso = peso
        self.Altura = Altura
        self.Estilo = Estilo

    def insertar_caracteristicas(self):
        cursor.execute("INSERT INTO Caracteristicas (id_caracteristicas, id_participantes, nombre, peso, altura, estilo) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.id_caracteristicas, self.id_participante, self.nombre, self.peso, self.Altura, self.Estilo))
        conexion.commit()
        print("Datos insertados correctamente.")
    def actualizar_caracteristicas(self, peso, altura, Estilo):
        cursor.execute("UPDATE Caracteristicas SET peso = ? and SET altura = ? and SET Estilo = ? WHERE id_caracteristicas = ?", (peso, altura, Estilo, self.id_caracteristicas))
        conexion.commit()
        print("Datos actualizados correctamente.")
    def eliminar_de_caracteristicas(self):
        cursor.execute("DELETE FROM Caracteristicas WHERE id_caracteristicas = ?", (self.id_caracteristicas,))
        conexion.commit()
        print("Datos eliminados correctamente.")
class combates:
    def __init__(self, id_combate, id_participante1, id_participante2, Nombres,nombre2,Tipo_de_combate):
        self.id_combate = id_combate
        self.id_participante1 = id_participante1
        self.id_participante2 = id_participante2
        self.Nombres = Nombres
        self.nombre2 = nombre2
        self.Tipo_de_combate = Tipo_de_combate
        

    def insertar_combates(self):
        cursor.execute("INSERT INTO Combates (id_combate, id_participante1, id_participante2, Nombres, nombre2, Tipo_de_combate) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.id_combate, self.id_participante1, self.id_participante2, self.Nombres, self.nombre2, self.Tipo_de_combate))
        conexion.commit()
        print("Datos insertados correctamente.")
    def actualizar_combates(self, Nombres, nombre2, Tipo_de_combate):
        cursor.execute("UPDATE Combates SET Nombres = ? and SET nombre2 = ? and SET Tipo_de_combate = ? WHERE id_combate = ?", (Nombres, nombre2, Tipo_de_combate, self.id_combate))
        conexion.commit()
        print("Datos actualizados correctamente.")
    def eliminar_de_combates(self):
        cursor.execute("DELETE FROM Combates WHERE id_combate = ?", (self.id_combate,))
        conexion.commit()
        print("Datos eliminados correctamente.")
conexion.close()

# participantes
consultar_participantes = Participantes(1, 1, "David", "theGrefg")
consultar_participantes.consultar_participantes("fila", "resultado")
# combates