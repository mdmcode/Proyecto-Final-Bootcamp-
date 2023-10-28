import json

materias = ['ingles', 'matematicas', 'cultura general']
preguntas = []
respuestas = []

def cargarArchivo(nombre):
    global preguntas
    with open(nombre, "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)

vidaDragon = 100
vidaJugador = 100
gana = False

def obtenerMaterias():
    texto = f"¿Que materia desea escoger?"
    for m in materias:
        texto += f"\n {m}"

    texto += '\n'
    return texto

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
    materia = input(obtenerMaterias())
    cargarArchivo('materias/' + materia + '.json')
    for pregunta in preguntas:
        print(preguntas[str(pregunta)]["pregunta"])
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

while len(materias) > 0:
    play()