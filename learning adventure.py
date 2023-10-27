import random
import json

pregunta = ''
respuesta = ''
fila = 0
listaElegida = []
preguntas = []
respuestas = []

def cargarArchivo(nombre):
    global preguntas
    with open(nombre, "r") as archivo:
        preguntas = json.load(archivo)

def obtenerPregunta(lista):
    lista = lista.sort()
    
    # Establece la pregunta y su respectiva respuesta
    for pregunta in range(len(lista)):
        preguntas.append(lista[pregunta][0])
        respuestas.append(lista[pregunta][1])

        lista.remove(pregunta)
        lista.remove(respuesta)

    # return respuesta

vidaDragon = 100
vidaJugador = 100
gana = False

def obtenerOpciones(opciones):
    letras = ['a) ', 'b) ', 'c)']
    for pregunta in range(len(opciones)):
        print(f"{letras[pregunta]} {opciones[pregunta]}")

def comprobarVictoria(rJugador, r):
    global vidaJugador, vidaDragon, gana
    if rJugador.lower() == r.lower():
        print("¡Correcto!")
        vidaDragon = vidaDragon - 5
        print(f"Atacaste al dragon, tiene {vidaDragon} de vida")
        return True
    else:
        print("Incorrecto")
        vidaJugador = vidaJugador - 5
        print(f"Te han atacado, tiene {vidaJugador} de vida")
        return False

def play():
    materia = input("¿Que materia desea escoger?\n Ingles\n Matematicas\n Cultura General\n")
    cargarArchivo('materias/' + materia + '.json')
    for pregunta in preguntas:
        print(preguntas[str(pregunta)]["pregunta"])
        obtenerOpciones(preguntas[str(pregunta)]["opciones"])
        response = input() 
        gana = comprobarVictoria(response, preguntas[str(pregunta)]["respuesta"])
        if gana == False:
            print(preguntas[str(pregunta)]["info"])

    if vidaDragon > vidaJugador:
        print("Has perdido")
    elif vidaJugador > vidaDragon:
        print("Has derrotado al dragon")
    else:
        play()

play()