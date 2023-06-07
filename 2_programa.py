#precioDeLaManzana:int = 10
#cantidadDeManzanas: int = 5
#print ("Vas a pagar")
#print(precioDeLaManzana*cantidadDeManzanas)
""" 
    Comentario multilineas 
    
"""
#concatenacion
#precioDeManzana:int=int(input("Precio de la manzana: "))
#cantidadDeManzanas:int=int(input("Cantidad de manzanas: "))
#print("vas a pagar")
#print("las manzanas estan en : " + str(precioDeManzana))
"""print("las manzanas estan en: ", precioDeManzana)
print(f"las manzanas estan en: {precioDeManzana} y fueron: {cantidadDeManzanas}")
print("las manzanas estan en : ")
print(precioDeManzana)
print("y fueron")
print(cantidadDeManzanas)
print("total a pagar")
print(precioDeManzana*cantidadDeManzanas)"""
manzanasCompradas:int=int(input("Cuantas manzanas compro: "))
precioManzanas:int=float(input("Precio de la manzana: "))
if manzanasCompradas >=10:
    print("!Tienes descuento¡")
    print((precioManzanas*manzanasCompradas)*.10)
    descuento=((precioManzanas*manzanasCompradas)*.10)
print(f"Compraste: {manzanasCompradas} y las manzanas cuestan: {precioManzanas}")
print("Pagas")
print((precioManzanas*manzanasCompradas)-descuento)
