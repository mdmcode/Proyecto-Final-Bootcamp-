rotuloPregunta = None

### Listas de preguntas ###
ingles = [['Traduce: CASA', 'House'], 
            ['Traduce: CARRO', 'car'], 
            ['Traduce: MADRE', 'Mom'],
            ['Traduce: MANZANA', 'Apple'],
            ['Traduce: HABITACIÓN', 'Room'],
            ['Traduce: AZÚCAR', 'Sugar']
        ]
mates = [['Raíz cuadrada de 9', '3'], 
        ['2 + 2', '4'], 
        ['2 X 4', '8'],
        ['¿Cuantos segundos hay en un minuto?', '60'],
        ['2 X 2 + 10', '14'],
        ['¿Cuantos angulos tiene un triangulo?', '3'],
        ['El único numero primo par', '2']
        ]
general = [['¿Cuantos huesos tiene el cuerpo humano?', '206'], 
            ['¿Cuanto acabó la segunda guerra mundial', '1945'], 
            ['¿En que fecha se celebra la independencia en Colombia?', '20 de Julio'],
            ['¿En que año se descubrió América?', '1492'],
            ['¿Cual es el pais mas grande del mundo?', 'Rusia'],
            ['¿Cual es el animal más grande del planeta?', 'Ballena azul'],
            ['¿Cual es la capital de Colombia?', 'Bogotá']
            ]

opcionesIngles = [['Hosing', 'House', 'Tree'], 
                  ['Audi', 'Wheel', 'Car'],
                  ['Mom', 'Mami', 'Nana'],
                  ['Apple', 'Mango', 'Apol'],
                  ['Habitation', 'Room', 'Living'],
                  ['Sweet', 'Sour', 'Sugar']]

opcionesMates = [['9', '3', 'No tiene'],
                 ['4', '2', '7'],
                 ['16', '70', '8'],
                 ['80', '60', '100'],
                 ['24', '38', '12'],
                 ['3', '180', '360'],
                 ['6', '2', '8']]

opcionesGeneral = [['365', '206', '50'],
                   ['2004', '1845', '1945'],
                   ['7 de agosto', '1 de Enero', '20 de julio'],
                   ['1492', '1955', '2018'],
                   ['China', 'Rusia', 'Colombia'],
                   ['Ballena azul', 'Elefante', 'Hormiga'],
                   ['Cali', 'Bogotá', 'Buenaventura']]

BarraDelDragon = None
BarraDelPrincipe = None
pregunta = ''
preguntasUsadas = []
opciones = []
respuesta = ''
fila = 0
print(len(ingles))

# Toma un parametro con el nombre de la materia o conjunto de palabras
def obtenerPregunta(lista):
    global rotuloPregunta, pregunta, opciones, respuesta, fila, preguntasUsadas
    print(lista)
    #Compara el parametro con las listas existentes
    if lista == 'ingles':
        #Obtiene un valor aleatorio de fila y toma una pregunta y su respuesta
        fila = rangoAleatorio(0, len(ingles))
        opciones = opcionesIngles[fila]
        pregunta = ingles[fila][0]     
        respuesta = ingles[fila][1]
        print(opciones)
    elif lista == 'matematicas':
        fila = rangoAleatorio(0, len(mates))
        opciones = opcionesMates[fila]
        pregunta = mates[fila][0]
        respuesta = mates[fila][1]
    elif lista == 'cultura general':
        fila = rangoAleatorio(0, len(general))
        opciones = opcionesGeneral[fila]
        pregunta = general[fila][0]     
        respuesta = general[fila][1]
    
    #print(opciones,fila,pregunta)
    rotuloPregunta = Label(pregunta, 90, 360, tamaño=10, negrito=True)
    
    if pregunta in preguntasUsadas:
        pass
    else:
        pass
        #print(pregunta)
    preguntasUsadas.append(pregunta)

    if lista == 'ingles':
        ingles.remove(ingles[fila])
    elif lista == 'matematicas':
        mates[fila].remove(pregunta)
    elif lista == 'cultura general':
        general[fila].remove(pregunta)

    return respuesta

vidaDragon = 100
vidaJugador = 100

def obtenerOpciones():
    # global opcionA, opcionB, opcionC
    opcionA.valor = 'a) ' + opciones[0]
    opcionB.valor = 'b) ' + opciones[1]
    opcionC.valor = 'c) ' + opciones[2]

def comprobarVictoria(rJugador, r):
    global vidaJugador, vidaDragon
    if rJugador.lower() == r.lower():
        print("¡Correcto!")
        vidaDragon = vidaDragon - 5
        BarraDelDragon.ancho -= 5
    else:
        print("Incorrecto")
        vidaJugador = vidaJugador - 5
        BarraDelPrincipe.ancho -= 5

opcion = ''

materia = ''
opcionA = None
opcionB = None
opcionC = None

def onKeyPress(key):
    global opcion
    if key == 'a':
        opcion = opciones[0]
        comprobarVictoria(opcion, respuesta)
    elif key == 'b':
        opcion = opciones[1]
        comprobarVictoria(opcion, respuesta)
    elif key == 'c':
        opcion = opciones[2]
        comprobarVictoria(opcion, respuesta)


def onMousePress(x, y):
    global opcionA, opcionB, opcionC, rotuloPregunta
    for boton in botones:
        if boton.toca(x, y):
            materia = boton.nombre
            #print(materia)
            dibujarBatalla()
            respuesta = obtenerPregunta(materia)
            BarraDelDragon = Rect(30, 85, 100, 16, relleno=gradiente('verdePrimavera', 'verdeAmarillento'))
            BarraDelPrincipe = Rect(205, 180, 90, 16, relleno=gradiente('verdePrimavera', 'verdeAmarillento'))
            #print(opciones)
            opcionA = Rotulo(f"a) {opciones[0]}", 207, 302, relleno='grisPizarraOscuro', tamaño=20)
            opcionB = Rotulo(f"b) {opciones[1]}", 207, 330, relleno='grisPizarraOscuro', tamaño=20)
            opcionC = Rotulo(f"c) {opciones[2]}", 207, 360, relleno='grisPizarraOscuro', tamaño=20)
            # obtenerOpciones()

if vidaDragon == 0:
    print("Tú ganas")
elif vidaJugador == 0:
    print("El dragón gana")
