from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from src.weather import get_weather

app = Flask(__name__)
CORS(app)

def conectar_db():
    return sqlite3.connect('sql/base.db')

@app.route('/registrar', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    print(data)
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO usuarios (nombre, tipo_identificacion, numero_identificacion, contrasena, fecha_nacimiento)
                       VALUES (?, ?, ?, ?, ?)""", (
                           data['nombre'],
                           data['tipoIdentificacion'],
                           data['numeroIdentificacion'],
                           data['contrasena'],
                           data['fechaNacimiento']
                           ))
        conn.commit()
        return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        if conn:
            conn.close()


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Ciudad no especificada'}), 400
    data = get_weather(city)
    return jsonify(data)


@app.route('/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    print("Datos recibidos:", data)

    numero_identificacion = data.get('numeroIdentificacion')
    contrasena = data.get('contrasena')

    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT contrasena FROM usuarios WHERE numero_identificacion = ?", (numero_identificacion,))
        resultado = cursor.fetchone()
        print("Resultado de la consulta:", resultado)

        if resultado and resultado[0] == contrasena:
            return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
        else:
            return jsonify({'error': 'Credenciales incorrectas'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:
            conn.close()

@app.route('/agendar', methods=['POST'])
def agendar_cita():
    data = request.get_json()
    print("Datos recibidos para agendar cita:", data)

    tipo_cita = data.get('tipoCita')
    doctor_id = data.get('doctorCita')
    fecha = data.get('fechaCita')
    hora = data.get('horaCita')
    usuario_id = data.get('usuarioId')  # Este debe venir del frontend o sesión

    try:
        conn = conectar_db()
        cursor = conn.cursor()

        # Insertar horario
        cursor.execute("""
            INSERT INTO horarios (doctor_id, fecha, hora)
            VALUES (?, ?, ?)
        """, (doctor_id, fecha, hora))
        horario_id = cursor.lastrowid

        # Insertar cita
        cursor.execute("""
            INSERT INTO citas (usuario_id, horario_id, tipo_cita)
            VALUES (?, ?, ?)
        """, (usuario_id, horario_id, tipo_cita))

        conn.commit()
        return jsonify({'mensaje': 'Cita agendada correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    finally:
        if conn:
            conn.close()

        
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port =5000)

