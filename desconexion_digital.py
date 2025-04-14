# elegir actividad
import random
actividades = ["dibujar","leer","caminar"]
actividad_elegida = random.choice(actividades)
print('tu actividad elegida es :', actividad_elegida)

# puntos de las actividades 
puntos = {
    "dibujar" : 10,
    "leer" : 20,
    "caminar" : 15,
}

mostrar_puntos = input('¿Qué actividad hiciste?:')
if mostrar_puntos in puntos: 
    print("¡Ganaste", puntos[mostrar_puntos], "puntos!")
else:
    print("Esa actividad no está registrada.")


# meta diaria
def verificar_meta(minutos):
    if minutos >= 30 :
        print('Felicitaciones nuevo logro desbloquedo')
    else:
        print('te falta',30 - minutos,'para un nuevo logro')

tiempo = int(input('cuantos minutos estuviste en office? :'))
verificar_meta(tiempo)