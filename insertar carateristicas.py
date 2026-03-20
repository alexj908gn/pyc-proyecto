import sqlite3

conexion = sqlite3.connect("la_velada.db")
cursor = conexion.cursor()

# Insertar un registro
cursor.execute('''
INSERT INTO Caracteristicas (id_caracteristicas, id_participantes, nombre,peso,Altura, Estilo) 
VALUES (?, ?, ?, ?,?,?)
''', (1, 1, "David", 88,170,"diestro"))


participantes = [
    (2, 2, "Samantha", 40,160,"ambidiestro"),
    (3, 3, "Carlos",80,170,"diestro"),
    (4, 4, "Ibia",83,173,"diestro")
]

cursor.executemany('''
INSERT INTO Caracteristicas (id_caracteristicas, id_participantes, nombre,peso,Altura, Estilo) 
VALUES (?, ?, ?, ?,?,?)
''', participantes)

conexion.commit()
conexion.close()