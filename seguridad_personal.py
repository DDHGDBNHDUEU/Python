# añadir nuevo contacto
contactos = ["milagros","bianca","cami"]

nuevo_contacto = input("ingrese otro contacto: ")
contactos.append(nuevo_contacto)
print("Los contactos son :", contactos)

# Verificar zona segura
zonas = {"Centro": "segura", "Barrio X": "peligrosa"}
zona = input("Ingrese una zona: ")
print("Estado:", zonas.get(zona, "desconocida"))

# Ruta más segura
ruta = ["Calle A", "Calle B"]
print("Ruta:", " → ".join(ruta))
