import psycopg2
from psycopg2.extras import RealDictCursor

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "legal_assistant_db",
    "user": "postgres",  # Reemplaza con tu usuario
    "password": "2tupackaos15T",  # Reemplaza con tu contraseña
    "host": "localhost",
    "port": "5432"
}

def save_query_to_db(query: str, response: str):
    """
    Saves the user query and the AI response to the database.
    """
    try:
        # Conectar a la base de datos
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Insertar la consulta y la respuesta
        query_sql = """
        INSERT INTO consultations (query, response)
        VALUES (%s, %s)
        """
        cursor.execute(query_sql, (query, response))
        conn.commit()

    except Exception as e:
        print(f"Database error: {e}")
        raise

    finally:
        # Cerrar la conexión
        if conn:
            cursor.close()
            conn.close()