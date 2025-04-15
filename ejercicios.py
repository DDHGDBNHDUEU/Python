# funcion para saludar
def saludar(nombre):
    print("hola",nombre)
saludar("mayra")

# calculadora basica
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese una operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "No se puede dividir por cero"
else:
    resultado = "Operación no válida"

print("Resultado:", resultado)

# lista de compras
producto1 = input("Producto 1: ")
producto2 = input("Producto 2: ")
producto3 = input("Producto 3: ")

lista = [producto1, producto2, producto3]

print("Lista de compras:")
for item in lista:
    print(item.upper())

# numeros pares
print("Números pares del 0 al 10:")
for i in range(0, 11):
    if i % 2 == 0:
        print(i)

# contar vocales
palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra tiene {contador} vocales.")

