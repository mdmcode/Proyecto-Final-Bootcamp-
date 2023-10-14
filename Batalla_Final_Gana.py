from cmu_graphics import *
from cmu_graphics import cmu_graphics

def dibujarVictoria():
    app.fondo = gradiente('índigo', 'azulPizarraOscuro', 'azulMedianoche', inicio='inferior')

    #LUNA
    Luna = Grupo(
    Círculo(50, 100, 30, relleno=gradiente('negro', 'gris', inicio='izquierda')),
    Círculo(40, 80, 3, relleno=rgb(50, 50, 50)),
    Círculo(65, 85, 4, relleno=rgb(85, 85, 85)),
    Círculo(70, 110, 3, relleno=rgb(85, 85, 85)),
    Círculo(40, 115, 4, relleno=rgb(45, 45, 45)),
    Círculo(45, 95, 4, relleno=rgb(55, 55, 55)),
    Círculo(60, 100, 4, relleno=rgb(75, 75, 75)),
    Círculo(30, 95, 3, relleno=rgb(15, 15, 15))
        )
    Luna.altura = 100
    Luna.ancho = 100
    Luna.centroY = 60
    Luna.centroX = 200

    #Estrellas
    Estrella(320, 50, 2, 5, relleno='blanco')
    Estrella(230, 115, 3, 5, relleno='blanco')
    Estrella(50, 325, 2, 5, relleno='blanco')
    Estrella(10, 25, 2, 5, relleno='blanco')

    #PLATAFORMA
    Rect(200, 280, 200, 200, relleno='grisPizarra')
    Poligono(200, 280, 110, 280, 135, 300, 150, 310, 130, 325, 155, 360, 135, 390, 200, 400, 
    relleno=gradiente('grisPizarra', 'grisPizarraOscuro', inicio="derecha"))
    Poligono(215, 360, 240, 301, 320, 310, 275, 320, 
    relleno=gradiente('grisPizarra', 'grisPizarraOscuro', inicio="izquierda"))
    Poligono(280, 387, 263, 365, 235, 375, 
    relleno=gradiente('grisPizarra', 'grisPizarraOscuro', inicio="izquierda"))
    Poligono(360, 320, 325, 332, 290, 330, 
    relleno=gradiente('grisPizarra', 'grisPizarraOscuro', inicio="izquierda"))

    DragonMalo = Grupo(
        ##PATAS
        Poligono(170, 320, 130, 370, 130, 395, 170, 390, 170, 375,
        relleno=gradiente('carmesí', 'rojoOscuro')),
        Poligono(190, 320, 230, 370, 230, 395, 190, 390, 190, 360,
        relleno=gradiente('carmesí', 'rojoOscuro')),
        Poligono(130, 370, 120, 340, 143, 355, relleno=gradiente('carmesí', 'rojoOscuro', 'grisPizarraOscuro', inicio="inferior")),
        Poligono(230, 370, 240, 340, 217, 355, relleno=gradiente('carmesí', 'rojoOscuro', 'grisPizarraOscuro', inicio="inferior")),
        
        ##ALA IZQUIERDA
        Poligono(150, 250, 135, 235, 125, 220, 115, 205, 105, 180, 
        105, 80, 60, 125, 40, 160, 25, 205, 20, 230, 20, 255, 45,310,55, 245, 80, 310, 90, 255, 115, 325, 120,
        260, 140, 315, borde='grisPizarraOscuro', anchuraDeBorde=5, relleno=gradiente('cian', 'azulMedianoche', 'azulAcero')),
        ##Vena1
        Linea(80, 310, 74, 250, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(74, 250, 65, 190, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(65, 160, 80, 130, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(65, 190, 65, 160, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(80, 130, 105, 80, relleno=gradiente("rojo", 'rojoOscuro')),
        ##Vena2
        Linea(45, 310, 35, 245, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(45, 187, 55, 157, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(69, 125, 105, 80, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(35, 245, 45, 187, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(55, 157, 69, 125, relleno=gradiente("rojo", 'rojoOscuro')),
        ##Vena3
        Linea(115, 325, 105, 250, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(91, 188, 90, 165, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(90, 135, 105, 80, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(105, 250, 91, 188, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(90, 165, 90, 135, relleno=gradiente("rojo", 'rojoOscuro')),
        
        ##ALA DERECHA
        Poligono(210, 250, 225, 235, 235, 220, 245, 205, 255, 180, 255, 80, 300, 125, 320, 160, 335, 205, 340, 
        230, 340, 255, 315, 310, 305, 245, 280, 310, 270, 255, 245, 325, 240, 260, 220, 315,
        borde='grisPizarraOscuro', anchuraDeBorde=5, relleno=gradiente('cian', 'azulMedianoche', 'azulAcero')),
        
        ##Vena1
        Linea(280, 310, 286, 250, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(286, 250, 295, 190, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(295, 160, 280, 130, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(295, 190, 295, 160, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(280, 130, 255, 80, relleno=gradiente("rojo", 'rojoOscuro')),
        ##Vena2
        Linea(315, 310, 325, 245, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(315, 187, 305, 157, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(291, 125, 255, 80, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(325, 245, 315, 187, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(305, 157, 291, 125, relleno=gradiente("rojo", 'rojoOscuro')),
        ##Vena3
        Linea(245, 325, 255, 250, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(269, 188, 270, 165, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(270, 135, 255, 80, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(255, 250, 269, 188, relleno=gradiente("rojo", 'rojoOscuro')),
        Linea(270, 165, 270, 135, relleno=gradiente("rojo", 'rojoOscuro')),
        
        ##CUERPO
        Óvalo(180, 297, 80, 160, relleno=gradiente('carmesí', 'rojoOscuro')),
        Óvalo(180, 297, 65, 130, relleno=gradiente('rojo','carmesí', 'rojoOscuro')),
        
        ##Cuernos
        Poligono(120, 160, 125, 85, 160, 120, relleno=gradiente('tomate', 'rojoOscuro', inicio="inferior")),
        Poligono(240, 160, 240, 85, 200, 120, relleno=gradiente('tomate', 'rojoOscuro', inicio="inferior")),
        Poligono(200, 120, 200, 100, 185, 120, relleno=gradiente('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
        Poligono(160, 120, 165, 100, 175, 120, relleno=gradiente('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
        Poligono(119, 200, 110, 170, 130, 180, relleno=gradiente('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
        Poligono(240, 200, 250, 170, 225, 180, relleno=gradiente('grisPizarraClaro', 'rojoOscuro', inicio="inferior")),
        
        #CABEZA
        Poligono(160, 240, 119, 200, 130, 180, 120, 160, 160, 120, 200, 120, 240, 160, 225, 180, 240, 200, 200, 240, 
        relleno=gradiente('carmesí', 'rojoOscuro')),

        ##BOCA
        Óvalo(180, 200, 50, 20, relleno="rojoOscuro"),
        Poligono(154, 200, 206, 200, 200, 214, 190, 222, 170, 222, 160, 215, relleno="rojoOscuro"),
        Poligono(170, 222, 174, 205, 178, 222, relleno=gradiente("blanco", 'ladrillo', inicio="superior")),
        Poligono(190, 222, 185, 205, 180, 222, relleno=gradiente("blanco", 'ladrillo', inicio="superior")),
        Poligono(175, 190, 180, 210, 185, 190, relleno=gradiente("blanco", 'ladrillo', inicio="inferior")),
        Poligono(195, 190, 190, 208, 184, 190, relleno=gradiente("blanco", 'ladrillo', inicio="inferior")),
        Poligono(163, 190, 169, 210, 175, 190, relleno=gradiente("blanco", 'ladrillo', inicio="inferior")),
        Poligono(190, 222, 196, 204, 200, 215, relleno=gradiente("blanco", 'ladrillo', inicio="superior")),
        Poligono(169, 222, 163, 204, 160, 215, relleno=gradiente("blanco", 'ladrillo', inicio="superior")),
        
        ##OJOS
        Poligono(150, 145, 170, 175, 145, 160, relleno=gradiente('azulGandul','rojoOscuro', 'negro')),
        Poligono(210, 145, 190, 175, 215, 160, relleno=gradiente('azulGandul', 'rojoOscuro', 'negro')),
        Poligono(216, 165, 190, 185, 220, 173, relleno=gradiente('azulGandul', 'rojoOscuro', 'negro')),
        Poligono(144, 165, 170, 185, 140, 173, relleno=gradiente('azulGandul', 'rojoOscuro', 'negro')),
        )
    DragonMalo.altura = 160
    DragonMalo.ancho = 160
    DragonMalo.centroX = 80
    DragonMalo.centroY = 190

#PRINCESA
Poligono(320, 280, 340, 240, 360, 280, relleno='violeta')
Circulo(340, 230, 15, relleno='caqui')
Linea(325, 213, 355, 213, anchuraDeLinea=20, guion=True, relleno='oro')
Rect(325, 213, 30, 13, relleno='oro')

#PRINCIPE
Linea(235, 255, 210, 225, relleno='azulAceroClaro')
Linea(223, 255, 232, 242, relleno='azulAceroClaro')
Rect(240, 240, 20, 40, relleno='rojo')
Circulo(250, 225, 15, relleno='caqui')
Linea(235, 213, 261, 213, anchuraDeLinea=20, guion=True, relleno='oro')
Rect(235, 213, 30, 13, relleno='oro')

# cmu_graphics.run()