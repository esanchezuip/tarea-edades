# 1. Lista con al menos 5 nombres
nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]

# 2. Diccionario: nombre -> edad
edades = {
    nombres[0]: 30,
    nombres[1]: 25,
    nombres[2]: 22,
    nombres[3]: 35,
    nombres[4]: 28,
}

# 3. Solicitar un nombre al usuario
nombre = input("Ingresa un nombre: ").strip().capitalize()

# 4. Mostrar la edad o un mensaje si no existe
if nombre in edades:
    print(f"{nombre} tiene {edades[nombre]} años.")
else:
    print(f"{nombre} no fue encontrado.")