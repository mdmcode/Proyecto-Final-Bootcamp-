from cmu_graphics import *
from cmu_graphics import cmu_graphics

botonGeneral = Group(
        Rect(21,240,120,40,relleno='gainsBoro',borde='marrónCuero'),
        Label('Cultura general',80,260,tamaño=14)
    )
botonGeneral.nombre = 'cultura general'

botonIngles = Group(
        Rect(170,240,60,40,relleno='gainsBoro',borde='marrónCuero'),
        Label('Ingles',200,260,tamaño=14)
    )
botonIngles.nombre = 'ingles'

botonMates = Group(
        Rect(260,240,110,40,relleno='gainsBoro',borde='marrónCuero'),
        Label('Matematicas',315,260,tamaño=14)
    )
botonMates.nombre = 'matematicas'

botones = Group(botonGeneral, botonIngles, botonMates)
botones.visible = False

def selección():
    global botones, botonMates, botonIngles, botonGeneral
    Rect(0,0,400,400,relleno=gradient('nebulosaRosa','varillaDoradaPalida',inicio='superior'),borde='marrónCuero',anchuraDeBorde=5)

    botones.visible = True

    Label('¿Que actividad prefieres para combatir?',200,200,tamaño=18)
    Label('¡Suerte en tú combate!',200,340,tamaño=16)
    Label('Haz click en una de las opciones para iniciar',200,310,tamaño=16)
    #estrella
    Star(200,380,15,5,relleno='oro',borde='negro')
    #SIMBOLO RESTA
    Line(345,25,375,45,relleno='azulVioleta',anchuraDeLinea=6)
    #SIMBOLO SUMA
    Line(40,320,40,354,relleno ='aguaMarinaMedio',anchuraDeLinea=7)
    Line(25,337,55,337,relleno ='aguaMarinaMedio',anchuraDeLinea=7)

    #SIMBOLO MULTIPLICACION
    Line(146,130,170,160,relleno='coral',anchuraDeLinea=5)
    Line(170,130,145,160,relleno='coral',anchuraDeLinea=5)

    #BANDERA JAPON
    Rect(35,30,65,40,relleno='blanco')
    Circle(68,50,14,relleno='rojo')

    #BANDERA SUECIA
    Rect(280,120,65,40,relleno='azulReal')
    Line(280,140,345,140,relleno='amarillo',anchuraDeLinea=5)
    Line(300,120,300,160,relleno='amarillo',anchuraDeLinea=5)

    Polygon(215,50,245,50,230,20,relleno='rosadoFuerte')
    Circle(50,150,18,relleno=gradient('limaVerde','azulReal','verde',inicio='superior'))
