import mysql.connector
opcionBaseDeDatos=1
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
try:
    conexion=mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        port=port,
        database=database)
    cursor=conexion.cursor()
    cursor.execute("Select * from materia")
    registros=cursor.fetchall()
    for registro in registros:
        print(f'id {registro[0]} valor {registro[1]} ')
   
except mysql.connector.Error as err:
    print("Ocurrio un error al conectar: ", err)
finally:
    conexion.close()
