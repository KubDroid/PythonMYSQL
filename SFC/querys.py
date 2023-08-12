from decouple import config

user=config('MYSQL_USER')
password=config('MYSQL_PASSWORD')
host=config('MYSQL_HOST')
db=config('MYSQL_DB')
port=config('MYSQL_PORT')

#print(config('MYSQL_USER'))
#print(password)
#print(host)
#print(db)
#print(port)

# importaciones
import mysql.connector
from mysql.connector import Error

# Conectar a la base de datos
try: 
    conexiondb = mysql.connector.connect(user=user,
                                         password=password,
                                         host=host, 
                                         db=db,
                                         port=port
                                         )
    
    if conexiondb.is_connected():    
        print("Conexión correcta \n"  + "Host:" + host + " " + "Port:" + port)  
        infoserver = conexiondb.get_server_info()
        print("Info del servidor:",infoserver)
     

# creación del cursor
    cursor = conexiondb.cursor()
    cursor.execute("SELECT name, countrycode FROM city ")
    for name, countrycode in cursor.fetchall():
        print(name, "|", countrycode)



except mysql.connector.Error as e:
        print("No puedo conectar a la base de datos:",e)
     

# Cerrar Conección a la base de datos
finally:
    if conexiondb.is_connected():
        conexiondb.close() # Se cerro la conexión as la BD.
        print("La conexión ha finalizado.")