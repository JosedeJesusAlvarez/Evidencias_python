import mysql.connector
opcionBaseDeDatos=1
def conexionBd(opcionBaseDeDatos):
    if opcionBaseDeDatos==1:
        host="localhost"
        user="root"
        password=""
        port=3306
        database='mini-siiau'
    elif opcionBaseDeDatos==2:
        host= "142.44.163.242"
        user="Alumno1"
        password="AlumnoPython1@."
        port=4000
        database='mini-siiau'
    conexion=mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        port=port,
        database=database)
    return conexion