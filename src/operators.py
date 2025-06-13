from basedDatos import connection

def insertUsuarios(nombre, tipo_identificacion, numero_identificacion, contrasena, fecha_nacimiento):
    connec = connection()
    cursor = connec.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, tipo_identificacion, numero_identificacion, contrasena, fecha_nacimiento) VALUES (?, ?, ?, ?, ?)", (nombre, tipo_identificacion, numero_identificacion, contrasena, fecha_nacimiento))
    connec.commit()
    connec.close()
    
def get_horarios_disponibles():
    con = connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM horarios WHERE disponible = 1")
    resultados = cursor.fetchall()
    con.close()
    return resultados

def validacion_users(numero_identificacion, contrasena):
    con = connection()
    cursor = con.cursor()
    cursor.execute("SELECT FROM * usuarios WHERE numero_identificacion = ? AND contrasena = ?", (numero_identificacion, contrasena))
    usuario = cursor.fetchone()
    con.close()
    return usuario

def registro_citas(usuario_id, horario_id, motivo):
    con = connection()
    cursor = con.cursor()
    cursor.execute("SELECT disponible FROM horarios WHERE id = ?", (horario_id,))
    estado = cursor.fetchone()
    if estado and estado[0] == 1:
        cursor.execute(
            "INSERT INTO citas (usuario_id, horario_id, motivo) VALUES (?, ?, ?)", (usuario_id, horario_id, motivo)
        
        )
        cursor.execute("UPDATE horarios SET disponible = 0 WHERE id = ?", (horario_id,))
        con.commit()
        resultado = True
    else:
        resultado = False 
        con.close()
        return resultado
    
def citas_usuario(usuario_id):
        con = connection()
        cursor = con.cursor()
        cursor.execute(
            """ 
            SELECT citas.id, horarios.fecha, horarios.hora, citas.motivo FROM citas 
            JOIN horarios ON citas.horario_id = horarios.id
            WHERE citas.usuario_id = ?
            """, (usuario_id,)
        )
        citas = cursor.fetchall()
        con.close()
        return citas
    
def cancelacion(cita_id):
        con = connection()
        cursor = con.cursor()
        cursor.execute("SELECT horario_id FROM citas WHERE id = ?", (cita_id))
        horario = cursor.fetchone()
        if horario:
            horario_id = horario[0]

            cursor.execute("DELETE FROM citas WHERE id = ?", (cita_id,))
            cursor.execute("UPDATE horarios SET disponible = 1 WHERE id = ?", (horario_id, ))
            con.commit()
            resultado = True
        else:
            resultado = False
        con.close()
        return resultado

def insertar_doctor(nombre, especialidad):
    try:
        con = connection()
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO doctores (nombre, especialidad)
            VALUES (?, ?)
        """, (nombre, especialidad))
        con.commit()
        con.close()
        return True
    except Exception as e:
        print("Error al insertar doctor:", e)
        return False
