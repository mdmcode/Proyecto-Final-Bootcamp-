from cmu_graphics import *

#CASTILLO
# imagen= Imagen('cmu://612287/25324480/castillo2.jpg', -30, 160)

# imagen.ancho = 280
# imagen.altura = 239
# imagen.centroY = 227
# imagen.centroX = 100

def dibujarCastillo():
    #CAMINO
    Rect(0, 320, 400, 320, relleno=gradiente('marVerde', 'marVerdeOscuro'))
    Rect(0, 320, 400, 320, relleno="verde")

    #TORRE-DERECHA
    Rect(245, 130, 100, 190, relleno='azulAlica', borde="grisOscuro", anchuraDeBorde=3)
    Poligono(335, 55, 290, 20, 250, 55, relleno='turquesa', borde="grisOscuro")
    Rect(235, 117, 120, 20, relleno='grisOscuro')
    Rect(235, 55, 110, 16, relleno='grisOscuro')
    Rect(255, 70, 76, 50, relleno='azulAlica', borde="grisOscuro")
    Circulo(347, 63, 8, relleno='grisOscuro')
    Circulo(238, 63, 8, relleno='grisOscuro')
    Circulo(354, 127, 10, relleno='grisOscuro')
    Circulo(236, 127, 10, relleno='grisOscuro')

    #TORRE-CENTRAL
    Rect(150, 118, 70, 80, relleno='azulAlica', borde="grisOscuro", anchuraDeBorde=3)

    #BASE
    Rect(120, 195, 130, 125, relleno='azulAlica', borde="grisOscuro", anchuraDeBorde=5)

    #TORRE-IZQUIERDA
    Rect(33, 130, 90, 190, relleno='azulAlica', borde="grisOscuro", anchuraDeBorde=3)
    Rect(40, 70, 76, 50, relleno='azulAlica', borde="grisOscuro")
    Circulo(130, 127, 10, relleno='grisOscuro')
    Circulo(27, 127, 10, relleno='grisOscuro')
    Rect(30, 55, 100, 16, relleno='grisOscuro')
    Circulo(30, 63, 8, relleno='grisOscuro')
    Circulo(129, 63, 8, relleno='grisOscuro')
    Rect(25, 117, 105, 20, relleno='grisOscuro')

    Poligono(33, 55, 77, 20, 125, 55, relleno='turquesa', borde="grisOscuro")
    Polygon(320, 80, 340, 80, 358, 100, 375, 97, 400, 135, 400, 130, 357, 115, relleno=gradiente('varillaDoradaClaraAmarilla', 'varillaDoradaPálida', inicio="inferior"))
