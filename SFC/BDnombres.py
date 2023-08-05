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

# Conectar a la base de datos
try: 
    conexionDb = mysql.connector.connect(user=user,
                                         password=password,
                                         host=host, 
                                         port=port)
    print("Conexión correcta \n"  + "Host:" + host + " " + "Port:" + port)  

     

except mysql.connector.Error as e:
	print("No puedo conectar a la base de datos:",e)
	


cursor = conexionDb.cursor()
cursor.execute("show databases")

for bd in cursor: # type: ignore
    print(bd)
    
    
# Cerrar Conección a la base de datos
conexionDb.close()