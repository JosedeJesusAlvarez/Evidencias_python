cantidadDeManzanas:int=int(input("Cuantas manaznas se vendio: "))
while cantidadDeManzanas != 0 :
    precioDeLasManzanas:int=float(input("Las manzanas cuestan:  "))
    nombre=input("Nombre del comprador: ")
    if cantidadDeManzanas==18:
        descuento=(precioDeLasManzanas*cantidadDeManzanas)*.20
        print(f"Tienes descuento secreto de: {descuento}%")
        print(f"Pagaras:{(precioDeLasManzanas*cantidadDeManzanas)-descuento} pelucholares")
    elif nombre=="Elizabeth":
        descuento=((precioDeLasManzanas*cantidadDeManzanas)*.20)
        print(f"Descuento Especial: {descuento}%")
        print(f"Pagaras:{(precioDeLasManzanas*cantidadDeManzanas)-descuento} pelucholares")
    elif cantidadDeManzanas>=10:
        descuento=(precioDeLasManzanas*cantidadDeManzanas)*.10
        print(f"Descuento: {descuento}%")
        print(f"Pagaras:{(precioDeLasManzanas*cantidadDeManzanas)-descuento} pelucholares")

    else:
        descuento=0 
    print(f"pagaras {precioDeLasManzanas*cantidadDeManzanas} pelucholares")
    cantidadDeManzanas:int=int(input("Cuantas manzanas se vendio: "))