from cmu_graphics import *
from cmu_graphics import cmu_graphics

Rect(0,0,400,400,relleno=gradiente('nebulosaRosa','varillaDoradaPalida',inicio='superior'),borde='marrónCuero',anchuraDeBorde=5)

botonGeneral = Group(
    Rect(21,240,120,40,relleno='gainsBoro',borde='marrónCuero'),
    Rotulo('Cultura general',80,260,tamaño=14)
)
botonGeneral.nombre = 'cultura general'

botonIngles = Group(
    Rect(170,240,60,40,relleno='gainsBoro',borde='marrónCuero'),
    Rotulo('Ingles',200,260,tamaño=14)
)
botonIngles.nombre = 'ingles'

botonMates = Group(
    Rect(260,240,110,40,relleno='gainsBoro',borde='marrónCuero'),
    Rotulo('Matematicas',315,260,tamaño=14)
)
botonMates.nombre = 'Matematicas'

botones = Group(botonGeneral, botonIngles, botonMates)

Rotulo('¿Que actividad prefieres para combatir?',200,200,tamaño=18)
Rotulo('¡Suerte en tú combate!',200,310,tamaño=16)
Rotulo('Haz click en una de las opciones para iniciar',200,310,tamaño=16)
#estrella
Estrella(200,380,15,5,relleno='oro',borde='negro')
#SIMBOLO RESTA
Linea(345,25,375,45,relleno='azulVioleta',anchuraDeLinea=6)
#SIMBOLO SUMA
Linea(40,320,40,354,relleno ='aguaMarinaMedio',anchuraDeLinea=7)
Linea(25,337,55,337,relleno ='aguaMarinaMedio',anchuraDeLinea=7)
#SIMBOLO DIVICION
Circulo(365,315,5,relleno='azulGandul')
Linea(345,318,367,32,relleno='azulGandul',anchuraDeLinea=5)
Circulo(349,336,5,relleno='azulGandul')
#SIMBOLO MULTIPLICACION
Linea(146,130,170,160,relleno='coral',anchuraDeLinea=5)
Linea(170,130,145,160,relleno='coral',anchuraDeLinea=5)

#BANDERA JAPON
Rect(35,30,65,40,relleno='blanco')
Circulo(68,50,14,relleno='rojo')

#BANDERA SUECIA
Rect(280,120,65,40,relleno='azulReal')
Linea(280,140,345,140,relleno='amarillo',anchuraDeLinea=5)
Linea(300,120,300,160,relleno='amarillo',anchuraDeLinea=5)

Poligono(215,50,245,50,230,20,relleno='rosadoFuerte')
Circulo(50,150,18,relleno=gradiente('limaVerde','azulReal','verde',inicio='superior'))

#cmu_graphics.run()