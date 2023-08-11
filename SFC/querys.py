from Conexion import *

# creación del cursor
cursor = conexionDb.cursor()
cursor.execute("SELECT name, countrycode FROM city ")
for name, countrycode in cursor.fetchall():
    print(name, "|", countrycode)

conexionDb.close()