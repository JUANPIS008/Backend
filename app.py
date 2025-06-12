from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

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
        
if __name__ == '__main__':
    app.run(debug=True)
