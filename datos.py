import sqlite3

conexion = sqlite3.connect("la_velada.db")
cursor = conexion.cursor()
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar participante")
        print("2. Actualizar participante")
        print("3. Eliminar participante")
        print("4. Consultar participante")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_p = int(input("ID participante: "))
            id_c = int(input("ID características: "))
            nombre = input("Nombre: ")
            canal = input("Canal: ")

            p = Participantes(id_p, id_c, nombre, canal)
            p.insertar_participantes()

        elif opcion == "2":
            id_p = int(input("ID participante a actualizar: "))
            nombre = input("Nuevo nombre: ")
            canal = input("Nuevo canal: ")

            p = Participantes(id_p, None, None, None)
            p.actualizar_participantes(nombre, canal)

        elif opcion == "3":
            id_p = int(input("ID participante a eliminar: "))
            p = Participantes(id_p, None, None, None)
            p.eliminar_de_participantes()

        elif opcion == "4":
            id_p = int(input("ID participante a consultar: "))
            p = Participantes(id_p, None, None, None)
            p.consultar_participantes(None, None)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta otra vez.")
class Participantes :
    def __init__(self, id_participantes, id_caracteristicas, Nombre, canal_de_internet):
        self.id_participantes = id_participantes
        self.id_caracteristicas = id_caracteristicas
        self.Nombre= Nombre
        self.canal_de_internet = canal_de_internet


    def insertar_participantes(self):
        cursor.execute("INSERT INTO Participantes (id_participantes,id_caracteristicas,Nombre, canal_de_internet) VALUES (?, ?, ?, ?)",
                       (self.id_participantes, self.id_caracteristicas, self.Nombre, self.canal_de_internet))
        conexion.commit()
        print("Datos insertados correctamente.")
    def actualizar_participantes(self,Nombre, canal_de_internet):
        cursor.execute("UPDATE Participantes SET Nombre = ? and SET canal_de_internet = ? WHERE id_participantes = ?", (Nombre, canal_de_internet, self.id_participantes))
        conexion.commit()
        print("Datos actualizados correctamente.")
    def eliminar_de_participantes(self):
        cursor.execute("DELETE FROM Participantes WHERE id_participantes = ?", (self.id_participantes,))
        conexion.commit()
        print("Datos eliminados correctamente.")
    def consultar_participantes(self,fila,resultado):
        cursor.execute("SELECT * FROM Participantes WHERE id_participantes = ?", (self.id_participantes,))
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
print("Bienvenido al sistema de gestión de la Velada del Año")
llamar = menu()
def menu():
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar participante")
        print("2. Actualizar participante")
        print("3. Eliminar participante")
        print("4. Consultar participante")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_p = int(input("ID participante: "))
            id_c = int(input("ID características: "))
            nombre = input("Nombre: ")
            canal = input("Canal: ")

            p = Participantes(id_p, id_c, nombre, canal)
            p.insertar_participantes()

        elif opcion == "2":
            id_p = int(input("ID participante a actualizar: "))
            nombre = input("Nuevo nombre: ")
            canal = input("Nuevo canal: ")

            p = Participantes(id_p, None, None, None)
            p.actualizar_participantes(nombre, canal)

        elif opcion == "3":
            id_p = int(input("ID participante a eliminar: "))
            p = Participantes(id_p, None, None, None)
            p.eliminar_de_participantes()

        elif opcion == "4":
            id_p = int(input("ID participante a consultar: "))
            p = Participantes(id_p, None, None, None)
            p.consultar_participantes(None, None)

        elif opcion == "5":
            print("Saliendo del programa...")
            break
        elif opcion == "6":
        else:
            print("Opción no válida. Intenta otra vez.")

conexion.close()


