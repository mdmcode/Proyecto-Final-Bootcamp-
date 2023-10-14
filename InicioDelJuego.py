from cmu_graphics import *
from cmu_graphics import cmu_graphics

historia = ['En una aldea muy lejana',
            'encuentra un gran castillo', 
            'en el cual vive una princesa',
            ]

def iniciar():
    #FONDO CASTILLO
    Rect(0,0,400,400,relleno=gradiente('azulCieloClaro','azulAlica',inicio='superior'))
    Rect(0,320,400,320,relleno=gradiente('verde','verdeMilitar',inicio='inferior'))
    #CASTILLO

    castillo=Grupo(
        Rect(0,160,50,170,relleno=gradiente('grisOscuro','grisTurbio',inicio='izquierda')),
        Rect(110,160,35,170,relleno=gradiente('grisOscuro','grisTurbio',inicio='izquierda')),
        Rect(135,200,50,130,relleno=gradiente('grisOscuro','grisTurbio',inicio='izquierda')),
        Rect(40,210,85,110,relleno='grisOscuro',borde='grisTurbio'),
        Rect(27,250,110,80,relleno='grisOscuro',borde='grisTurbio'),
        Rect(40,200,16,10,relleno='grisTurbio'),
        Rect(70,200,22,10,relleno='grisTurbio'),
        Rect(105,200,19,10,relleno='grisTurbio'),
        Poligono(60,160,0,80,0,160,relleno=gradiente('coral','marronCuero',inicio='izquierda')),
        Poligono(100,160,155,160,125,100,relleno=gradiente('coral','marrónCuero',inicio='izquierda')),
        Poligono(126,200,194,200,160,170,relleno=gradiente('coral','marrónCuero',inicio='superior')),
        
        #PRINCIPE
        Rect(280, 280, 20, 40, relleno='rojo'),
        Circulo(290, 270, 15, relleno="caqui"),
        Linea(275, 250, 305, 250, anchuraDeLinea=20, guion=True, relleno='oro'),
        Rect(275, 250, 30, 13, relleno='oro'),
        
        Ovalo(60,230,20,28,borde='marrónCuero'),
        Ovalo(105,230,20,28,borde='marrónCuero'),
        Rect(50,237,20,10,relleno='grisOscuro'),
        Rect(50,237,20,10,relleno='grisOscuro'),
        Rect(95,237,20,10,relleno='grisOscuro'),
        Rect(60,280,45,50,relleno='chocolate',borde='marronCuero'),
        Linea(83,280,83,330,relleno='marrónCuero'),
        
        Ovalo(160,225,20,30,borde='marrónCuero'),
        Ovalo(160,280,15,25,borde='marrónCuero'),
        Ovalo(18,195,25,40,borde='marrónCuero'),
        Ovalo(127,175,15,30,borde='marrónCuero'),
        Ovalo(45,270,10,15,borde='marrónCuero'),
        Ovalo(120,270,10,15,borde='marrónCuero'),
        Poligono(200,320,240,320,220,280,relleno='violeta'),
        Circulo(220,270,15,relleno='caqui')
        
    )

iniciar()
cmu_graphics.run()