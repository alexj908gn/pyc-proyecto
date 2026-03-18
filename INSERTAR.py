import sqlite3

conexion = sqlite3.connect("la_velada.db")
cursor = conexion.cursor()

# Insertar un registro
cursor.execute('''
INSERT INTO Participantes (id_participantes, id_caracteristicas, nombre, canal_de_internet) 
VALUES (?, ?, ?, ?)
''', (4, 1, "Juan", "mari"))

# Insertar múltiples registros
participantes = [
    (1, 2, "Ana", "negro"),
    (2, 3, "Luis", "aguacate"),
    (3, 4, "Marta", "ibai")
]

cursor.executemany('''
INSERT INTO Participantes (id_participantes, id_caracteristicas, nombre, canal_de_internet) 
VALUES (?, ?, ?, ?)
''', participantes)

conexion.commit()
conexion.close()