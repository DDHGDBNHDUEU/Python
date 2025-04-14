# informar problema
reportes = { }
problema = input('ingresa el problema que quiere informar :')

if problema in reportes:
    reportes[problema] += 1
else:
    reportes[problema] = 1

print('el reporte es :',reportes)

# prioridad de reportes 
prioridad = {
    "bache": "alta",
    "luz rota": "media",
    "calle cortada":"media",
    "semáforo": "alta",}

print('problemas con prioridad alta:')
for problema, nivel in prioridad.items():
    if nivel == "alta":
        print("-", problema)

# ubi gps
latitud = float(input("Ingresá la latitud: "))
longitud = float(input("Ingresá la longitud: "))

ubicacion = {
    "latitud": latitud,
    "longitud": longitud
}
print('tu ubicacion es:', ubicacion)
