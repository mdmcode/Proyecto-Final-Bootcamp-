from cmu_graphics import *
from cmu_graphics import cmu_graphics

def dibujarBatalla():
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
    
    #ELECCIONES
    Rect(0, 280, 400, 220, relleno='limónChifón', borde='plateado', anchuraDeBorde=5)
    
    Pregunta = Rotulo("Pregunta", 80, 305, relleno='grisPizarraOscuro', tamaño=20)
    EleccionA = Rotulo("a)", 207, 302, relleno='grisPizarraOscuro', tamaño=20)
    EleccionB = Rotulo("b)", 207, 330, relleno='grisPizarraOscuro', tamaño=20)
    EleccionC = Rotulo("c)", 207, 360, relleno='grisPizarraOscuro', tamaño=20)
    
    Dragon = Grupo(
        #MANDIBULA
        Poligono(275, 247, 275, 230, 270, 218, 253, 217, 245, 217, 237, 215,227, 215, 215, 215, 202, 215, 190, 215, 172, 215, 
        157, 220, 147, 215, 0, 230, relleno=gradiente('carmesí', 'ladrillo', inicio='inferior')),
        
        #CUERPO
        Poligono(0, 320, 45, 290, 26, 257, 0, 260, relleno=gradiente('ladrillo', 'salmón', inicio='inferior'), borde='rojoOscuro'),
        Poligono(40, 300, 76, 268, 50, 235, 26, 257, relleno=gradiente('ladrillo', 'salmón', inicio='inferior'),borde='rojoOscuro'),
        Poligono(50, 235, 78, 220, 95, 250, 75, 275, relleno=gradiente('ladrillo', 'salmón', inicio='inferior'),borde='rojoOscuro'),
        Poligono(78, 220, 110, 200, 119, 239, 93, 260, relleno=gradiente('ladrillo', 'salmón', inicio='inferior'),borde='rojoOscuro'),
        Poligono(110, 200, 155, 180, 155, 228, 117, 248, relleno=gradiente('ladrillo', 'salmón', inicio='inferior'),borde='rojoOscuro'),
        Poligono(0, 260, 26, 257, 50, 235, 78, 220, 110, 200, 141, 190, 145, 180, 120, 175, 140, 160, 93, 164, 77, 170, 57, 175, 40, 187, 30, 198, 8, 212, 0, 216, relleno=gradiente('rojoOscuro', 'carmesí', inicio='inferior')),
        Poligono(115, 163, 106, 148, 100, 145, 85, 130, 65, 120, 88, 145, 93, 165, relleno=gradiente('granate', 'marrón')),
        Poligono(100, 164, 75, 157, 63, 161, 48, 155, 62, 168, 57, 175, relleno=gradiente('granate', 'marrón')),
        Poligono(65, 170, 43, 168, 31, 159, 10, 150, 37, 173, 40, 187, relleno=gradiente('granate', 'marrón')),
        Poligono(44, 185, 27, 185, 20, 188, 11, 183, 14, 196, 8, 212, 30, 198, relleno=gradiente('granate', 'marrón')),
        Poligono(20, 205,0, 203, 0, 216, relleno=gradiente('granate', 'marrón')),
        
        #CABEZA
        Poligono(150, 240, 140, 250, 160, 240, 155, 250, 170, 240, 176, 230, 185, 230, 190, 227, 200, 227, 210, 230, 217,
        228, 225, 230, 240, 230, 255, 235, 260, 235, 275, 247, relleno=gradiente('carmesí', 'ladrillo', inicio='inferior')),
        
        Poligono(172, 215, 157, 220, 147, 215, 150, 200, 170, 203, relleno="rojoOscuro"),
        
        Poligono(135, 135, 140, 160, 120, 175, 145, 180, 135, 197, 155, 193, 140, 220, 165, 195, 213, 180, 252, 178,
        273, 180, 285, 160, 268, 145, 253, 149, 250, 156, 245, 160, 238, 165, 230, 165, 220, 160, 210, 170, 197, 163,
        195, 163, 190, 158, 167, 155, 165, 155, 135, 135, relleno=gradiente('carmesí', 'ladrillo', inicio='inferior')),
        
        Poligono(150, 200, 158, 210, 173, 205, 180, 207, 190, 205, 203, 195, 213, 180, 
        relleno=gradiente('carmesí', 'ladrillo', inicio='inferior')),
        Poligono(190, 200, 213, 178, 252, 178, 273, 180, 290, 210, 272, 200, 
        relleno=gradiente('carmesí', 'ladrillo', inicio='derecha-inferior')),
        Poligono(285, 201, 273, 180, 285, 160, 285, 160, 285, 160, 
        relleno=gradiente('carmesí', 'ladrillo', inicio='derecha')),
        Linea(285, 160, 268, 145, relleno=gradiente('carmesí', 'ladrillo', inicio='derecha-inferior')),
        Poligono(268, 145, 253, 147, 250, 156, 245, 160, 238, 165, 230, 165, 220, 160, relleno=gradiente('carmesi', 'marrónArenoso', inicio='inferior')),
        Poligono(197, 163, 190, 158, 167, 155, 162, 155),
        Poligono(163, 155, 160, 170, 165, 195, 190, 200, 196, 200, 172, 190, relleno='rojoOscuro'),
        
        #NARIZ
        Poligono(270, 165, 260, 162, 260, 152, 270, 155, 270, 165, relleno=gradiente('carmesi', 'negro', inicio='derecha-superior')),
        
        #CUERNOS
        Poligono(197, 163, 167, 155, 165, 140, 168, 127, 253, 149, 235, 156, 220, 160, 
        relleno=gradiente('coralClaro', 'rojo', inicio='superior')),
        Linea(165, 140, 235, 156, relleno='negro', opacidad=50),
        Linea(175, 157, 170, 140, relleno='negro', opacidad=50),
        Linea(170, 140, 175, 130, relleno='negro', opacidad=50),
        Linea(190, 161, 185, 145, relleno='negro', opacidad=50),
        Linea(185, 145, 190, 133, relleno='negro', opacidad=50),
        Linea(201, 157, 198, 147, relleno='negro', opacidad=50),
        Linea(198, 147, 201, 135, relleno='negro', opacidad=50),
        Linea(215, 155, 213, 150, relleno='negro', opacidad=50),
        Linea(213, 150, 215, 138, relleno='negro', opacidad=50),
        Linea(225, 155, 230, 143, relleno='negro', opacidad=50),
        Poligono(167, 155, 155, 143, 147, 138, 135, 127, 127, 117, 145, 123, 150, 128, 165, 140, 
        relleno=gradiente('blancoAntiguo', 'coralClaro','marrónArenoso', inicio='superior')),
        Poligono(165, 140, 150, 128, 135, 112, 125, 95, 168, 127, 
        relleno=gradiente('blancoAntiguo', 'coralClaro','marrónArenoso', inicio='superior')),
        
        #ALETA
        Poligono(135, 136, 140, 160, 120, 175, 145, 180, 135, 197, 155, 193, 147, 215, 165, 195,
        160, 170, 158, 165, 135, 136, relleno=gradiente('rojoOscuro', 'carmesí', inicio='izquierda')),
        Linea(135, 136, 160, 170, relleno='rojoOscuro'),
        Linea(120, 175, 160, 170, relleno='rojoOscuro'),
        Linea(135, 197, 160, 170, relleno='rojoOscuro'),
        Linea(165, 155, 135, 135, relleno='rojoOscuro'),
        Linea(135, 135, 140, 160, relleno='rojoOscuro'),
        Linea(140, 160, 120, 175, relleno='rojoOscuro'),
        Linea(120, 175, 145, 180, relleno='rojoOscuro'),
        Linea(145, 180, 135, 197, relleno='rojoOscuro'),
        Linea(135, 197, 155, 193, relleno='rojoOscuro'),
        Linea(155, 193, 140, 220, relleno='rojoOscuro'),
        Linea(140, 220, 165, 195, relleno='rojoOscuro'),
        
        #DIENTES
        Poligono(172, 215, 176, 208, 178, 215, relleno=gradiente('blancoAntiguo', 'rojo', inicio='inferior')),
        Poligono(182, 215, 185, 210, 187, 205, 191, 215, relleno=gradiente('blancoAntiguo', 'rojo', inicio='inferior')),
        Poligono(196, 200, 196, 210, 206, 200, relleno=gradiente('blancoAntiguo', 'rojo', inicio='superior')),
        Poligono(202, 215, 205, 210, 210, 205, 208, 215, relleno=gradiente('blancoAntiguo', 'rojo', inicio='inferior')),
        Poligono(217, 198, 212, 210, 220, 205, 225, 200, relleno=gradiente('blancoAntiguo', 'rojo', inicio='superior')),
        Poligono(220, 215, 223, 209, 225, 205, 227, 215, relleno=gradiente('blancoAntiguo', 'rojo', inicio='inferior')),
        Poligono(230, 200, 230, 210, 240, 200, 235, 197, relleno=gradiente('blancoAntiguo', 'rojo', inicio='superior')),
        Poligono(237, 215, 239, 207, 239, 205, 245, 217, relleno=gradiente('blancoAntiguo', 'rojo', inicio='inferior')),
        Poligono(245, 200, 243, 210, 248, 205, 251, 200, relleno=gradiente('blancoAntiguo', 'rojo', inicio='superior')),
        Poligono(250, 217, 251, 205, 251, 205, 257, 218, relleno=gradiente('blancoAntiguo', 'rojo', inicio='inferior')),
        Poligono(255, 200, 255, 210, 260, 205, 265, 200, relleno=gradiente('blancoAntiguo', 'rojo', inicio='superior')),
        Poligono(260, 220, 263, 210, 263, 205, 266, 220, relleno=gradiente('blancoAntiguo', 'rojo', inicio='inferior')),
        
        #OJO
        Poligono(195, 165, 210, 175, 225, 160, relleno=gradiente('rojoOscuro', 'rojo', inicio='inferior')),
        Poligono(220, 160, 210, 170, 195, 163, 207, 153, 220, 160, 
        relleno=gradiente('rojoNaranja','naranjaOscuro', 'oro', inicio="superior")),
        )
        
    Dragon.altura = 200
    Dragon.ancho= 210
    Dragon.centroX = 100
    Dragon.centroY = 200
    #PRINCESA
    Poligono(320, 280, 340, 240, 360, 280, relleno='violeta')
    Circulo(340, 230, 15, relleno='caqui')
    Linea(325, 213, 355, 213, anchuraDeLinea=20, guion=True, relleno='oro')
    Rect(325, 213, 30, 13, relleno='oro')
    
    #BARRAS DE VIDA
    BarraDelDragon = Rect(30, 85, 100, 16, relleno=gradiente('verdePrimavera', 'verdeAmarillento'))
    BarraDelPrincipe = Rect(205, 180, 90, 16, relleno=gradiente('verdePrimavera', 'verdeAmarillento'))
    
    #PRINCIPE
    Linea(235, 255, 210, 225, relleno='azulAceroClaro')
    Linea(223, 255, 232, 242, relleno='azulAceroClaro')
    Rect(240, 240, 20, 40, relleno='rojo')
    Circulo(250, 225, 15, relleno='caqui')
    Linea(235, 213, 261, 213, anchuraDeLinea=20, guion=True, relleno='oro')
    Rect(235, 213, 30, 13, relleno='oro')


