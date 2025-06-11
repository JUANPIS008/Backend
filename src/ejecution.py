from basedDatos import connection
def ejecution_script_sql():
    con = connection()
    cursor = con.cursor()

    with open('Backend/sql/base.sql', 'r', encoding='utf-8') as f:
        sql_script =f.read()
    
    cursor.executescript(sql_script)
    con.commit()
    con.close()
    print("Se han creado las tablas")

if __name__ == '__main__':
    ejecution_script_sql()