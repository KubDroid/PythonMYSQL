import mysql.connector
# Varibles para la coneccion
usuario='root'
clave ='M1SQL5819D4t4r00t'

conexion = mysql.connector.connect(user=usuario, password=clave,
                                   host='localhost', 
                                   database='practicas',
                                   port='3307')
    print(conexion)