from cmu_graphics import *
from cmu_graphics import cmu_graphics

def dibujarVictoria():
    app.fondo = gradient('índigo', 'azulPizarraOscuro', 'azulMedianoche', inicio='inferior')

    #LUNA
    Luna = Group(
    Circle(50, 100, 30, relleno=gradient('negro', 'gris', inicio='izquierda')),
    Circle(40, 80, 3, relleno=rgb(50, 50, 50)),
    Circle(65, 85, 4, relleno=rgb(85, 85, 85)),
    Circle(70, 110, 3, relleno=rgb(85, 85, 85)),
    Circle(40, 115, 4, relleno=rgb(45, 45, 45)),
    Circle(45, 95, 4, relleno=rgb(55, 55, 55)),
    Circle(60, 100, 4, relleno=rgb(75, 75, 75)),
    Circle(30, 95, 3, relleno=rgb(15, 15, 15))
        )
    Luna.altura = 100
    Luna.ancho = 100
    Luna.centroY = 60
    Luna.centroX = 200

    #Estrellas
    Star(320, 50, 2, 5, relleno='blanco')
    Star(230, 115, 3, 5, relleno='blanco')
    Star(50, 325, 2, 5, relleno='blanco')
    Star(10, 25, 2, 5, relleno='blanco')

    #PLATAFORMA
    Rect(200, 280, 200, 200, relleno='grisPizarra')
    Polygon(200, 280, 110, 280, 135, 300, 150, 310, 130, 325, 155, 360, 135, 390, 200, 400, 
    relleno=gradient('grisPizarra', 'grisPizarraOscuro', inicio="derecha"))
    Polygon(215, 360, 240, 301, 320, 310, 275, 320, 
    relleno=gradient('grisPizarra', 'grisPizarraOscuro', inicio="izquierda"))
    Polygon(280, 387, 263, 365, 235, 375, 
    relleno=gradient('grisPizarra', 'grisPizarraOscuro', inicio="izquierda"))
    Polygon(360, 320, 325, 332, 290, 330, 
    relleno=gradient('grisPizarra', 'grisPizarraOscuro', inicio="izquierda"))

    DragonMalo = Group(
        ##PATAS
        Polygon(170, 320, 130, 370, 130, 395, 170, 390, 170, 375,
        relleno=gradient('carmesí', 'rojoOscuro')),
        Polygon(190, 320, 230, 370, 230, 395, 190, 390, 190, 360,
        relleno=gradient('carmesí', 'rojoOscuro')),
        Polygon(130, 370, 120, 340, 143, 355, relleno=gradient('carmesí', 'rojoOscuro', 'grisPizarraOscuro', inicio="inferior")),
        Polygon(230, 370, 240, 340, 217, 355, relleno=gradient('carmesí', 'rojoOscuro', 'grisPizarraOscuro', inicio="inferior")),
        
        ##ALA IZQUIERDA
        Polygon(150, 250, 135, 235, 125, 220, 115, 205, 105, 180, 
        105, 80, 60, 125, 40, 160, 25, 205, 20, 230, 20, 255, 45,310,55, 245, 80, 310, 90, 255, 115, 325, 120,
        260, 140, 315, borde='grisPizarraOscuro', anchuraDeBorde=5, relleno=gradient('cian', 'azulMedianoche', 'azulAcero')),
        ##Vena1
        Line(80, 310, 74, 250, relleno=gradient("rojo", 'rojoOscuro')),
        Line(74, 250, 65, 190, relleno=gradient("rojo", 'rojoOscuro')),
        Line(65, 160, 80, 130, relleno=gradient("rojo", 'rojoOscuro')),
        Line(65, 190, 65, 160, relleno=gradient("rojo", 'rojoOscuro')),
        Line(80, 130, 105, 80, relleno=gradient("rojo", 'rojoOscuro')),
        ##Vena2
        Line(45, 310, 35, 245, relleno=gradient("rojo", 'rojoOscuro')),
        Line(45, 187, 55, 157, relleno=gradient("rojo", 'rojoOscuro')),
        Line(69, 125, 105, 80, relleno=gradient("rojo", 'rojoOscuro')),
        Line(35, 245, 45, 187, relleno=gradient("rojo", 'rojoOscuro')),
        Line(55, 157, 69, 125, relleno=gradient("rojo", 'rojoOscuro')),
        ##Vena3
        Line(115, 325, 105, 250, relleno=gradient("rojo", 'rojoOscuro')),
        Line(91, 188, 90, 165, relleno=gradient("rojo", 'rojoOscuro')),
        Line(90, 135, 105, 80, relleno=gradient("rojo", 'rojoOscuro')),
        Line(105, 250, 91, 188, relleno=gradient("rojo", 'rojoOscuro')),
        Line(90, 165, 90, 135, relleno=gradient("rojo", 'rojoOscuro')),
        
        ##ALA DERECHA
        Polygon(210, 250, 225, 235, 235, 220, 245, 205, 255, 180, 255, 80, 300, 125, 320, 160, 335, 205, 340, 
        230, 340, 255, 315, 310, 305, 245, 280, 310, 270, 255, 245, 325, 240, 260, 220, 315,
        borde='grisPizarraOscuro', anchuraDeBorde=5, relleno=gradient('cian', 'azulMedianoche', 'azulAcero')),
        
        ##Vena1
        Line(280, 310, 286, 250, relleno=gradient("rojo", 'rojoOscuro')),
        Line(286, 250, 295, 190, relleno=gradient("rojo", 'rojoOscuro')),
        Line(295, 160, 280, 130, relleno=gradient("rojo", 'rojoOscuro')),
        Line(295, 190, 295, 160, relleno=gradient("rojo", 'rojoOscuro')),
        Line(280, 130, 255, 80, relleno=gradient("rojo", 'rojoOscuro')),
        ##Vena2
        Line(315, 310, 325, 245, relleno=gradient("rojo", 'rojoOscuro')),
        Line(315, 187, 305, 157, relleno=gradient("rojo", 'rojoOscuro')),
        Line(291, 125, 255, 80, relleno=gradient("rojo", 'rojoOscuro')),
        Line(325, 245, 315, 187, relleno=gradient("rojo", 'rojoOscuro')),
        Line(305, 157, 291, 125, relleno=gradient("rojo", 'rojoOscuro')),
        ##Vena3
        Line(245, 325, 255, 250, relleno=gradient("rojo", 'rojoOscuro')),
        Line(269, 188, 270, 165, relleno=gradient("rojo", 'rojoOscuro')),
        Line(270, 135, 255, 80, relleno=gradient("rojo", 'rojoOscuro')),
        Line(255, 250, 269, 188, relleno=gradient("rojo", 'rojoOscuro')),
        Line(270, 165, 270, 135, relleno=gradient("rojo", 'rojoOscuro')),
        
        ##CUERPO
        Oval(180, 297, 80, 160, relleno=gradient('carmesí', 'rojoOscuro')),
        Oval(180, 297, 65, 130, relleno=gradient('rojo','carmesí', 'rojoOscuro')),
        
        ##Cuernos
        Polygon(120, 160, 125, 85, 160, 120, relleno=gradient('tomate', 'rojoOscuro', inicio="inferior")),
        Polygon(240, 160, 240, 85, 200, 120, relleno=gradient('tomate', 'rojoOscuro', inicio="inferior")),
        Polygon(200, 120, 200, 100, 185, 120, relleno=gradient('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
        Polygon(160, 120, 165, 100, 175, 120, relleno=gradient('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
        Polygon(119, 200, 110, 170, 130, 180, relleno=gradient('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
        Polygon(240, 200, 250, 170, 225, 180, relleno=gradient('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
        
        #CABEZA
        Polygon(160, 240, 119, 200, 130, 180, 120, 160, 160, 120, 200, 120, 240, 160, 225, 180, 240, 200, 200, 240, 
        relleno=gradient('carmesí', 'rojoOscuro')),

        ##BOCA
        Oval(180, 200, 50, 20, relleno="rojoOscuro"),
        Polygon(154, 200, 206, 200, 200, 214, 190, 222, 170, 222, 160, 215, relleno="rojoOscuro"),
        Polygon(170, 222, 174, 205, 178, 222, relleno=gradient("blanco", 'ladrillo', inicio="superior")),
        Polygon(190, 222, 185, 205, 180, 222, relleno=gradient("blanco", 'ladrillo', inicio="superior")),
        Polygon(175, 190, 180, 210, 185, 190, relleno=gradient("blanco", 'ladrillo', inicio="inferior")),
        Polygon(195, 190, 190, 208, 184, 190, relleno=gradient("blanco", 'ladrillo', inicio="inferior")),
        Polygon(163, 190, 169, 210, 175, 190, relleno=gradient("blanco", 'ladrillo', inicio="inferior")),
        Polygon(190, 222, 196, 204, 200, 215, relleno=gradient("blanco", 'ladrillo', inicio="superior")),
        Polygon(169, 222, 163, 204, 160, 215, relleno=gradient("blanco", 'ladrillo', inicio="superior")),
        
        ##OJOS
        Polygon(150, 145, 170, 175, 145, 160, relleno=gradient('azulGandul','rojoOscuro', 'negro')),
        Polygon(210, 145, 190, 175, 215, 160, relleno=gradient('azulGandul', 'rojoOscuro', 'negro')),
        Polygon(216, 165, 190, 185, 220, 173, relleno=gradient('azulGandul', 'rojoOscuro', 'negro')),
        Polygon(144, 165, 170, 185, 140, 173, relleno=gradient('azulGandul', 'rojoOscuro', 'negro')),
        )
    DragonMalo.altura = 160
    DragonMalo.ancho = 160
    DragonMalo.centroX = 80
    DragonMalo.centroY = 190

    #PRINCESA
    Polygon(320, 280, 340, 240, 360, 280, relleno='violeta')
    Circle(340, 230, 15, relleno='caqui')
    Line(325, 213, 355, 213, anchuraDeLinea=20, guion=True, relleno='oro')
    Rect(325, 213, 30, 13, relleno='oro')

    #PRINCIPE
    Line(235, 255, 210, 225, relleno='azulAceroClaro')
    Line(223, 255, 232, 242, relleno='azulAceroClaro')
    Rect(240, 240, 20, 40, relleno='rojo')
    Circle(250, 225, 15, relleno='caqui')
    Line(235, 213, 261, 213, anchuraDeLinea=20, guion=True, relleno='oro')
    Rect(235, 213, 30, 13, relleno='oro')
