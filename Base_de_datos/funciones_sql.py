import pandas as pd
import sqlite3

def esquema_tablas(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()

    # Obtener el esquema de cada tabla
    for (tabla,) in tablas:
        print(f"\nTabla: {tabla}")
        cursor.execute(f"PRAGMA table_info({tabla});")
        columnas = cursor.fetchall()
        for col in columnas:
            cid, name, tipo, notnull, dflt_value, pk = col
            print(f"  - {name} ({tipo}) {'PRIMARY KEY' if pk else ''}")
    
    return

def execute_query(query, cursor):
    cursor.execute(query)
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
    

    return 

def vista_rapida_query(query, conn, limite=5):
    """
    Ejecuta una consulta SQL sobre una conexión SQLite3 y muestra una vista rápida con pandas.

    Parámetros:
    - query (str): Consulta SQL a ejecutar.
    - conn (sqlite3.Connection): Objeto de conexión a la base de datos SQLite.
    - limite (int): Número de filas a mostrar. Default es 5.

    Retorna:
    - DataFrame con los resultados.
    """
    try:
        df = pd.read_sql_query(query, conn)
        display(df.head(limite))
        return 
    except Exception as e:
        print("Error al ejecutar la consulta:")
        print(e)
        return None