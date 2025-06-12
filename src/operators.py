from basedDatos import connection

def insertdUsuarios(usuario, contrasena):
    connec = connection()
    cursor = connec.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, contrasena))
    connec.commit()
    connec.close()
    
def get_horarios_disponibles():
    con = connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM horarios WHERE disponible = 1")
    resultados = cursor.fetchall()
    con.close()
    return resultados