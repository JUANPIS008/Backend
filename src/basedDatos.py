import sqlite3
import os 
def connection():
    ruta = os.path.join(os.path.dirname(__file__), '..', 'sql', 'base.db')
    connect = sqlite3.connect(ruta)
    return connect