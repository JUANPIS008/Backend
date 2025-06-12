from basedDatos import connection

def insertUsuarios(nombre, contrasena, tipo_identificacion, numero_identificacion, fecha_nacimiento):
    connec = connection()
    cursor = connec.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, contrasena, tipo_identificacion, numero_identificacion, fecha_nacimiento) VALUES (?, ?, ?, ?, ?)", (nombre, contrasena, tipo_identificacion, numero_identificacion, fecha_nacimiento))
    connec.commit()
    connec.close()
    
def get_horarios_disponibles():
    con = connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM horarios WHERE disponible = 1")
    resultados = cursor.fetchall()
    con.close()
    return resultados
def validacion_users():
    con = connection()
    cursor = con.cursor()
    cursor.execute("SELECT FROM * usuarios WHERE numero_identificacion = ? AND contrasena = ?", (numero_identificacion, contrasena))
    usuario = cursor.fetchone()
    con.close()
    return usuario