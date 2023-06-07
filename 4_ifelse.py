"""dia =input("Ingresa el dia de la semana: ")
#dia= "sabado"
if dia.lower == "miercoles" or dia== "lunes" :
    print("Toca curso")
elif dia== "viernes":
    print("toca curso")
    print("Toca peda")
elif dia=="sabado":
    print("Toca otra peda")
elif dia=="domingo":
    print("Toca ir a misa")
else :
    print("Toca descansar")
print("Adios")"""

cantidadDeManzanas:int=int(input("Cuantas manaznas compro: "))
precioDeLasManzanas:int=float(input("Las manzanas cuestan: "))
nombre=input("Nombre del comprador: ")
if cantidadDeManzanas==18:
    descuento=(precioDeLasManzanas*cantidadDeManzanas)*.20
    #print('Nota de venta'.center(60,x))
    print("Tienes descuento secreto: descuento del 20% ")
    print(descuento)
    print((precioDeLasManzanas*cantidadDeManzanas)-descuento)
elif nombre=="jose de jesus":
    descuento=((precioDeLasManzanas*cantidadDeManzanas)*.20)
    print("Descuento Especial del 20%")
    print(descuento)
    print((precioDeLasManzanas*cantidadDeManzanas)-descuento)
elif cantidadDeManzanas>=10:
    descuento=(precioDeLasManzanas*cantidadDeManzanas)*.10
    print("Descuento del 10%")
    print(descuento)
    print((precioDeLasManzanas*cantidadDeManzanas)-descuento)
else:
    descuento=0 
    print(precioDeLasManzanas*cantidadDeManzanas)