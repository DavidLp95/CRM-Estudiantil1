import sqlite3  # Importar el módulo sqlite3 para manejar la base de datos

def crear_conexion():
    """Crea y devuelve una conexión a la base de datos SQLite."""
    try:
        conexion = sqlite3.connect('estudiantes.db')  # Conectar a la base de datos 'estudiantes.db'
        return conexion  # Devolver el objeto de conexión
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")  # Imprimir error si ocurre
        return None  # Devolver None en caso de error

def crear_tabla():
    """Crea la tabla 'estudiantes' si no existe."""
    try:
        conexion = crear_conexion()  # Crear conexión a la base de datos
        if conexion is not None:
            cursor = conexion.cursor()  # Crear un cursor para ejecutar comandos SQL
            # Ejecutar comando SQL para crear la tabla 'estudiantes'
            cursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes (
                                id INTEGER PRIMARY KEY,  
                                nombres TEXT,  
                                apellidos TEXT,  
                                identificacion TEXT,  
                                edad INTEGER,  
                                programa TEXT,  
                                nota1 REAL, 
                                nota2 REAL,  
                                nota3 REAL,  
                                nota4 REAL,  
                                promedio REAL)''')  # Campo 'promedio' de tipo real
            conexion.commit()  # Confirmar los cambios en la base de datos
            conexion.close()  # Cerrar la conexión a la base de datos
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")  # Imprimir error si ocurre

crear_tabla()  # Llamar a la función para crear la tabla al ejecutar el script