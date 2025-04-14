# Ubipark - Estacionamiento Inteligente
# espacios libres
espacios = [True,True,False,True,False]

libres = espacios.count(True)

print('espacios libres:', libres)

# tarifa a pagar por hora
tarifa = 10
horas = int(input('ingrese cuantas horas desea reservar: '))
total = tarifa * horas
print('tiene que pagar:', total)

# reservar espacio
def reservar_espacio(lista_espacios, posicion):
    if 0 <= posicion < len(lista_espacios):
        if lista_espacios[posicion]:
            lista_espacios[posicion] = False
            print('Espacio reservado con éxito')
        else: 
            print('Ese espacio ya está ocupado')
    else:
        print('Número fuera de rango')
    
reservar = int(input('Cuatos espacios quiere reservar (del 0 al 4) :'))
reservar_espacio(espacios, reservar) 

#mostrar espacios 
def mostrar_espacios(lista_espacios):
    for i, estado in enumerate(lista_espacios):
        estado_str = "Libre" if estado else "Ocupado"
        print(f"Espacio {i}: {estado_str}")

print("Estado actual de los espacios:")
mostrar_espacios(espacios)
