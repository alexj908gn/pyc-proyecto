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


  

# Conexión a la base de datos
conexion = sqlite3.connect("la_velada.db")
cursor = conexion.cursor()

class Mostrar_Caracteristicas:

    def mostrar_todos(self):
        cursor.execute("SELECT * FROM caracteristicas")
        datos = cursor.fetchall()

        if datos:
            print("\n--- DATOS DE LA TABLA CARACTERISTICAS ---")
            for fila in datos:
                print(f"""
ID Caracteristicas: {fila[0]}
ID Participante: {fila[1]}
Nombre: {fila[2]}
Peso: {fila[3]}
Altura: {fila[4]}
Estilo: {fila[5]}
------------------------------""")
        else:
            print("No hay datos en la tabla.")

# 👉 Crear objeto
mostrar = Mostrar_Caracteristicas()

# 👉 Mostrar datos
mostrar.mostrar_todos()

# 👉 Cerrar conexión
conexion.commit()
conexion.close()