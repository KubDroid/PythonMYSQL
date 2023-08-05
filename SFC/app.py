from decouple import config

print("Host:" + config('MYSQL_HOST') + " " + "Port:" + config('MYSQL_PORT') )