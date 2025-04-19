import json
import time

roscos_disponibles = [
    "rosco_facil.json",
    "rosco_pokemon.json",
]

print("Tipos de rosco disponibles:")
for i, rosco in enumerate(roscos_disponibles, 1):
    print(f"{i}. {rosco.replace('.json', '')}")

opcion = input("\nElige el tipo de rosco: ").strip()

try:
    opcion = int(opcion)
    if opcion < 1 or opcion > len(roscos_disponibles):
        print("Opción no válida.")
        exit()
except ValueError:
    print("Opción no válida.")
    exit()

archivo_rosco = roscos_disponibles[opcion - 1]
with open(archivo_rosco, "r", encoding="utf-8") as f:
    preguntas = json.load(f)

estado = {letra: "pendiente" for letra in preguntas}
aciertos = 0
fallos = 0

print("\n=== Bienvenido a Mini-Pasapalabra ===")
print("Instrucciones: escribe la respuesta, 'pasapalabra' para pasar o 'salir' para terminar.\n")
input("Presiona Enter para comenzar...\n")

inicio = time.time()

while any(estado[l] == "pendiente" for l in preguntas):
    for letra in preguntas:
        if estado[letra] != "pendiente":
            continue

        definicion, respuesta = preguntas[letra]
        print(f"{letra}: {definicion}")
        user_input = input("Tu respuesta: ").strip().lower()

        if user_input == "salir":
            print("\nJuego terminado por el usuario.\n")
            break
        elif user_input == "pasapalabra":
            continue
        elif user_input == respuesta.lower():
            print("✅ ¡Correcto!\n")
            estado[letra] = "acertado"
            aciertos += 1
        else:
            print(f"❌ Incorrecto. La respuesta era: {respuesta}\n")
            estado[letra] = "fallado"
            fallos += 1
    else:
        continue
    break

fin = time.time()

tiempo_total = round(fin - inicio, 2)

print("\n=== Resultados del juego ===")
print(f"✅ Aciertos: {aciertos}")
print(f"❌ Fallos: {fallos}")
print(f"⏱️ Tiempo total: {tiempo_total} segundos")

print("\nGracias por jugar Pasapalabra versión Python :)\n")
