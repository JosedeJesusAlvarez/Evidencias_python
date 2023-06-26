import funcionDeConexion
import mysql.connector
def interfazSql(sql):
    try:
        conexion=funcionDeConexion.conexionBd(1)
        cursor=conexion.cursor()
        cursor.execute(sql)
        registros=cursor.fetchall()
        for registro in registros:
            print(registro)
   
    except mysql.connector.Error as err:
        print("Ocurrio un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()

interfazSql("Select name from maestro where name like 'M%'")