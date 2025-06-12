from basedDatos import connection

def insertdUsuarios(usuario, contrasena):
    connec = connection()
    cursor = connec.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, contrasena))
    connec.commit()
    connec.close()