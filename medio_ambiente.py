# calcular contaminacion
colillas = int(input("ingresa el numero de colillas: "))
agua = colillas * 1.5
print("Contaminación evitada: ", agua, "litros")

# meta de recoleccion 
meta = 75
if colillas >= 100 :
    print("Felicidades meta cumplida")

# calcular el porcentaje de avance
meta_total = int(input("Ingrese la meta total de colillas: "))
porcentaje = (colillas / meta_total) * 100
print("Avance hacia la meta: ", porcentaje, "%")