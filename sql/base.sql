CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo_identificacion TEXT NOT NULL,
    numero_identificacion INTEGER NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    fecha_nacimiento TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS doctores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    especialidad TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS horarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL,
    disponible INTEGER DEFAULT 1,
    FOREIGN KEY (doctor_id) REFERENCES doctores(id)
);

CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    horario_id INTEGER NOT NULL,
    tipo_cita TEXT NOT NULL,
    motivo TEXT,
    estado TEXT DEFAULT 'pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (horario_id) REFERENCES horarios(id)
);
