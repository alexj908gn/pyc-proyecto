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

class Insertar_Caracteristicas:
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
class actualizar_datos_participantes:
    def __init__(self, id_participante, nuevo_nombre):
        self.id_participante = id_participante
        self.nuevo_nombre = nuevo_nombre

    def actualizar_nombre(self):
        cursor.execute("UPDATE participantes SET nombre = ? WHERE id_participante = ?",
                       (self.nuevo_nombre, self.id_participante))
        conexion.commit()
        print("Nombre actualizado correctamente.")
    def actualizar_canal(self, nuevo_canal):
        cursor.execute("UPDATE participantes SET canal_de_internet = ? WHERE id_participante = ?",
                       (nuevo_canal, self.id_participante))
        conexion.commit()
        print("Canal actualizado correctamente.")
    def actualizar_id_caracteristica(self, nuevo_id_caracteristica):
        cursor.execute("UPDATE participantes SET id_caracteristicas = ? WHERE id_participante = ?",
                       (nuevo_id_caracteristica, self.id_participante))
        conexion.commit()
        print("ID Caracteristica actualizado correctamente.")

class actualizar_datos_caracteristicas:
    def __init__(self, id_participante, nuevo_peso, nueva_altura, nuevo_estilo):
        self.id_participante = id_participante
        self.nuevo_peso = nuevo_peso
        self.nueva_altura = nueva_altura
        self.nuevo_estilo = nuevo_estilo
    def actualizar_nombre(self, nuevo_nombre):
        cursor.execute("UPDATE caracteristicas SET nombre = ? WHERE id_participante = ?",
                       (nuevo_nombre, self.id_participante))
        conexion.commit()
        print("Nombre actualizado correctamente.")
    def actualizar_id_caracteristica(self, nuevo_id_caracteristica):
        cursor.execute("UPDATE caracteristicas SET id_caracteristicas = ? WHERE id_participante = ?",
                       (nuevo_id_caracteristica, self.id_participante))
        conexion.commit()
        print("ID Caracteristica actualizado correctamente.")
    def actualizar_peso(self, nuevo_peso):
        cursor.execute("UPDATE caracteristicas SET peso = ? WHERE id_participante = ?",
                       (nuevo_peso, self.id_participante))
        conexion.commit()
        print("Peso actualizado correctamente.")
    def actualizar_altura(self, nueva_altura):
        cursor.execute("UPDATE caracteristicas SET altura = ? WHERE id_participante = ?",
                       (nueva_altura, self.id_participante))
        conexion.commit()
        print("Altura actualizado correctamente.")
    def actualizar_estilo(self, nuevo_estilo):
        cursor.execute("UPDATE caracteristicas SET estilo = ? WHERE id_participante = ?",
                       (nuevo_estilo, self.id_participante))
        conexion.commit()
        print("Estilo actualizado correctamente.")
class actualizar_datos_combates:
    def __init__(self, id_combate, Tipo_de_combate):
        self.id_combate = id_combate
        self.Tipo_de_combate = Tipo_de_combate

    def actualizar_tipo(self):
        cursor.execute("UPDATE Combates SET Tipo_de_combate = ? WHERE id_combate = ?",
                       (self.Tipo_de_combate, self.id_combate))
        conexion.commit()
        print("Tipo de combate actualizado correctamente.")
    def actualizar_nombre2(self, nuevo_nombre):
        cursor.execute("UPDATE Combates SET nombre2 = ? WHERE id_combate = ?",
                       (nuevo_nombre, self.id_combate))
        conexion.commit()
        print("Nombre del segundo participante actualizado correctamente.")

class eliminar_datos_participantes:
    def __init__(self, id_participante):
        self.id_participante = id_participante

    def eliminar_participante(self):
        cursor.execute("DELETE FROM participantes WHERE id_participante = ?",
                       (self.id_participante,))
        conexion.commit()
        print("Participante eliminado correctamente.")
class eliminar_datos_caracteristicas:
    def __init__(self, id_participante):
        self.id_participante = id_participante

    def eliminar_caracteristica(self):
        cursor.execute("DELETE FROM caracteristicas WHERE id_participante = ?",
                       (self.id_participante,))
        conexion.commit()
        print("Caracteristica eliminada correctamente.")
class eliminar_datos_combates:
    def __init__(self, id_combate):
        self.id_combate = id_combate

    def eliminar_combate(self):
        cursor.execute("DELETE FROM Combates WHERE id_combate = ?",
                       (self.id_combate,))
        conexion.commit()
        print("Combate eliminado correctamente.")
class mostrar_datos_participantes:
    def mostrar_todos(self):
        cursor.execute("SELECT * FROM participantes")
        datos = cursor.fetchall()

        if datos:
            print("\n--- DATOS DE LA TABLA PARTICIPANTES ---")
            for fila in datos:
                print(f"""ID Participante: {fila[0]}
Nombre: {fila[1]}
Canal: {fila[2]}""")
        else:
            print("No hay datos en la tabla.")
class mostrar_datos_caracteristicas:
    def mostrar_todos(self):
        cursor.execute("SELECT * FROM caracteristicas")
        datos = cursor.fetchall()

        if datos:
            print("\n--- DATOS DE LA TABLA CARACTERISTICAS ---")
            for fila in datos:
                print(f"""ID Caracteristicas: {fila[0]} ID Participante: {fila[1]} Nombre: {fila[2]} Peso: {fila[3]} Altura: {fila[4]} Estilo: {fila[5]}""")
        else:
            print("No hay datos en la tabla.")
class mostrar_datos_combates:
    def mostrar_todos(self):
        cursor.execute("SELECT * FROM Combates")
        datos = cursor.fetchall()

        if datos:
            print("\n--- DATOS DE LA TABLA COMBATES ---")
            for fila in datos:
                print(f"""ID Combate: {fila[0]} ID Participante 1: {fila[1]} ID Participante 2: {fila[2]} Nombre Participante 1: {fila[3]} Nombre Participante 2: {fila[4]} Tipo de Combate: {fila[5]}""")
        else:
            print("No hay datos en la tabla.")
class llamar:
 # 👉 caracteristicas 
 caracteristicas_del_participante = Insertar_Caracteristicas()
# 👉 Insertar datos
 caracteristicas_del_participante.insertar_datos()


 #👉 participantes
 participantes = Insertar_Partcipantes()
 # 👉 Insertar datos
 participantes.insertar_datos()

#👉 Combates
combates = combates()
# 👉 Insertar datos
combates.insertar_datos()
#👉 Actualizar datos participante
caracteristicas_del_participante = actualizar_datos_participantes()

#👉 Actualizar datos caracteristicas
caracteristicas = actualizar_datos_caracteristicas(1,1 90, 180, "boxeo")

#👉 Actualizar datos combates
combates = actualizar_datos_combates()

conexion.close()
