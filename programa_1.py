#print("Hola, mundo")
#print("Jesus")
def tipo_de_cambio (precio_del_dolar, precio_peso):
    precio_dolar=(precio_del_dolar*precio_peso)
    return(precio_dolar)
precio_actual=tipo_de_cambio(18,1)
print(precio_actual)
precio_nuevo=tipo_de_cambio(25,1)
print(precio_nuevo)