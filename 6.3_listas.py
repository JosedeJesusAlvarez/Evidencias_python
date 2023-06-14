milista=[4,551,63,2,25,44,25]
print(milista)
print(milista[5])
print(len(milista))
milista.append(13)
print(milista)
#thislist.remove elimina el ultimo 
milista.sort()
for count, element in enumerate(milista):
    print(f"contador {count} element {element}")

if 4 in milista:
    print("Si, si esta!")
    print(milista.index(4))
    