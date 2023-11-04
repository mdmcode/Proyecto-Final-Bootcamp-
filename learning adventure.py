# Exportamos todos los archivos de gráficos y la librerías json y cmu_graphics
import json
from cmu_graphics import *
from cmu_graphics import cmu_graphics
import seleccionDeActividades
import Batalla_Final_Gana
import Batalla_Final_Pierde
import BatallaElecciones
import castillo
import InicioDelJuego
from seleccionDeActividades import botones
import time

InicioDelJuego.iniciar()
time.sleep(60)
seleccionDeActividades.selección()

# Definimos las listas
materias = ['ingles', 'matematicas', 'cultura general']
preguntas = []

# Definimos una función para abrir los archivos json con las preguntas
def cargarArchivo(nombre):
    global preguntas
    # Abre el archivo con el nombre del parametro
    with open(nombre, "r", encoding="utf-8") as archivo:
        # Carga el diccionaro del archivo en la lista preguntas
        preguntas = json.load(archivo)

# Definimos variables para comprobar la victoria
vidaDragon = 100
vidaJugador = 100
gana = False

# Nos ayuda a mostrar las opciones en pantalla
def obtenerOpciones(opciones):
    letras = ['a) ', 'b) ', 'c)']
    # Recorre la longitud del parametro recibido
    for pregunta in range(len(opciones)):
        for opcion in BatallaElecciones.opciones:
            opcion.valor = f"{letras[pregunta]} {opciones[pregunta]}"

# Compurueba si el jugador ganó
def comprobarVictoria(rJugador, r):
    global vidaJugador, vidaDragon, gana
    # Compara la respuesta del jugador con la respuesta correcta
    # Si son iguales le resta vida al dragon
    if rJugador.lower() == r.lower():
        print("¡Correcto!")
        vidaDragon = vidaDragon - 5
        print(f"Atacaste al dragon, tiene {vidaDragon} de vida")
        return True
    # De lo contrario le quita vida al jugador
    else:
        print("Incorrecto")
        vidaJugador = vidaJugador - 5
        print(f"Te han atacado, tiene {vidaJugador} de vida")
        return False

# Ejecuta el juego en sí
def play(materia):
    BatallaElecciones.dibujarBatalla()
    # Abre el archivo de preguntas de la materia escogida con el parametro
    cargarArchivo('materias/' + materia + '.json')
    # Recorre las preguntas
    for pregunta in preguntas:
        BatallaElecciones.rPregunta.valor = preguntas[str(pregunta)]["pregunta"]
        obtenerOpciones(preguntas[str(pregunta)]["opciones"])
        response = input() 
        gana = comprobarVictoria(response, preguntas[str(pregunta)]["respuesta"])
        if gana == False:
            print(preguntas[str(pregunta)]["info"])

    materias.remove(materia)
    if vidaDragon > vidaJugador:
        print("Has perdido")
    elif vidaJugador > vidaDragon:
        print("Has derrotado al dragon")
    else:
        play()

def enRatónPresionado(x, y):
    while len(materias) > 0:
        for boton in botones:
            if boton.touch(x, y):
                play(boton.nombre)

cmu_graphics.run()