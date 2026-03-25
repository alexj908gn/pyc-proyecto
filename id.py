import sqlite3

class CaracteristicasDB:

    def __init__(self, db_name):
        self.conexion = sqlite3.connect(db_name)
        self.cursor = self.conexion.cursor()

    # ✅ INSERTAR
    def insertar(self, id_caracteristicas, id_participante, nombre, peso, altura, estilo):
        self.cursor.execute(
            "INSERT INTO caracteristicas VALUES (?, ?, ?, ?, ?, ?)",
            (id_caracteristicas, id_participante, nombre, peso, altura, estilo)
        )
        self.conexion.commit()
        print("✅ Datos insertados.")

    # ✅ MOSTRAR TODOS
    def mostrar(self):
        self.cursor.execute("SELECT * FROM caracteristicas")
        datos = self.cursor.fetchall()

        if datos:
            print("\n--- TABLA CARACTERISTICAS ---")
            for fila in datos:
                print(f"""
ID: {fila[0]}
ID Participante: {fila[1]}
Nombre: {fila[2]}
Peso: {fila[3]}
Altura: {fila[4]}
Estilo: {fila[5]}
----------------------""")
        else:
            print("⚠️ No hay datos.")

    # ✅ BUSCAR POR NOMBRE
    def buscar(self, nombre):
        self.cursor.execute(
            "SELECT * FROM caracteristicas WHERE nombre = ?", (nombre,)
        )
        datos = self.cursor.fetchall()

        if datos:
            for fila in datos:
                print(fila)
        else:
            print("No encontrado.")

    # ✅ ACTUALIZAR
    def actualizar_peso(self, nombre, nuevo_peso):
        self.cursor.execute(
            "UPDATE caracteristicas SET peso = ? WHERE nombre = ?",
            (nuevo_peso, nombre)
        )
        self.conexion.commit()
        print("✅ Peso actualizado.")

    # ✅ ELIMINAR
    def eliminar(self, nombre):
        self.cursor.execute(
            "DELETE FROM caracteristicas WHERE nombre = ?", (nombre,)
        )
        self.conexion.commit()
        print("🗑️ Registro eliminado.")

    # ✅ CERRAR CONEXIÓN
    def cerrar(self):
        self.conexion.close()


# 👉 USO
db = CaracteristicasDB("la_velada.db")

# Insertar
db.insertar(2, 102, "Pedro", 80, 1.75, "Kickboxing")

# Mostrar
db.mostrar()

# Buscar
db.buscar("Pedro")

# Actualizar
db.actualizar_peso("Pedro", 85)

# Eliminar
db.eliminar("Pedro")

# Cerrar conexión
db.cerrar()