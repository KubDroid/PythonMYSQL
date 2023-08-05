# importaciones
import mysql.connector

# Varibles para la conexión
user = 'root'
password ='M1SQL5819D4t4r00t'
host = 'localhost'
port = '3307'
database = 'practicas'

# Conectar a la base de datos
try: 
    conexionDb = mysql.connector.connect(user = user,
                                         password = password,
                                         host = host, 
                                         database = database,
                                         port = port)
    print("Conexión correcta \n"  + "Host:" + host + " " + "Port:" + puerto)  

     

except mysql.connector.Error as e:
	print("No puedo conectar a la base de datos:",e)
	
 
# Cerrar Conección a la base de datos