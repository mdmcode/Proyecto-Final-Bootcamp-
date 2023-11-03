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
    
    #Estrellas
    Estrella(320, 50, 2, 5, relleno='blanco')
    Estrella(230, 115, 3, 5, relleno='blanco')
    Estrella(50, 325, 2, 5, relleno='blanco')
    Estrella(10, 25, 2, 5, relleno='blanco')
    
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
    
    #PLATAFORMA
    Poligono(200, 400, 400, 400, 400, 280, 200, 280, 200, 280, 110, 280,  135, 300, 150, 310, 130, 325, 155, 360, 135, 390, 200, 400,
    relleno=gradiente('grisPizarra', 'grisPizarraOscuro', inicio="izquierda")),
    Poligono(135, 390, 156, 373, 169, 355, 171, 340, 172, 326, 165, 315, 150, 310, 169, 296, 177, 315, 163, 327, 176, 340, 185, 360, 165, 383, 155, 392, 
    relleno=gradiente('grisPizarra', 'grisPizarraOscuro', inicio="izquierda")),
    Poligono(206, 357, 215, 340, 231, 347, 271, 338,277, 370, 208, 370,250, 385, relleno=gradiente('grisPizarra', 'grisPizarraOscuro', inicio='derecha')),
    Poligono(308, 320, 340, 328, 362, 328, 375, 335, 360, 350, 353, 330, 337, 342, 322, 340, 306, 358, 300, 340, 308, 320, 
    relleno=gradiente('grisPizarra', 'grisPizarraOscuro', inicio='derecha')),
    Poligono(150, 310, 110, 280, 400, 280, 400, 310, 322, 310, 308, 320, 262, 308, 250, 325, 220, 332, 245, 335, 251, 350, 258, 330, 268, 325, 278, 315, 
    295, 318, 322, 310, relleno=gradiente('tierra','marrónCuero', inicio='superior')),
    Poligono(135, 295, 115, 280, 400, 280, 400, 295, 200, 295, 217, 298, relleno=gradiente('verdeBosque','verde', inicio='izquierda'))
    
    #PRINCESA
    Princesa=Grupo(
             #vestido   
            Rect(180,140,40,60,fill='caqui'),
            Ovalo(220,190,8,35,fill='rosadoClaro',rotarAngulo=-45),
            Ovalo(182,190,8,35,fill='rosadoClaro',rotarAngulo=45),
            Ovalo(232,203,5,10,fill='marronArenoso',rotarAngulo=-45),
            Ovalo(170,203,5,10,fill='marronArenoso',rotarAngulo=45),
            Arc(200,200,200,200,140,80,fill='rosadoClaro'),
            Ovalo(234,239,20,96,fill='rosadoClaro',rotarAngulo=-40),
            Ovalo(168,239,20,96,fill='rosadoClaro',rotarAngulo=40),
            # Detalles
            Poligono(172,202,156,250,158,287,170,250,fill='rojoVioletaPalido',rotarAngulo=25),
            Poligono(200,218,190,250,200,300,210,250,fill='rojoVioletaPalido'),
            Poligono(231,200,232,250,244,286,246,250,fill='rojoVioletaPalido',rotarAngulo=-25),
            #corsel
            Poligono(200,220,215,209,215,180,185,180,185,209,fill='rojoVioletaPalido'),
            Ovalo(208,180,30,10,fill='white',rotarAngulo=15),
            Ovalo(192,180,30,10,fill='white',rotarAngulo=-15),
            Ovalo(200,179,33,8,fill='marronArenoso'),
            Line(200,165,200,180,fill='marronArenoso',anchuraDeLinea=10),
            Ovalo(200,183,7,10,fill='rosadoProfundo'),
            Star(202,181,4,4,fill='blanco'),
            Circle(200,151,15,fill='marronArenoso'),
            Ovalo(208,139,10,25,fill='caqui',rotarAngulo=-80),
            Ovalo(193,139,10,25,fill='caqui',rotarAngulo=80),
            #cara
            Line(198,146,192,150),
            Line(209,150,203,146),
            Ovalo(197,152,3,5),
            Ovalo(205,152,3,5),
            Ovalo(201,160,4,7),
            #corona
            Poligono(180,138,200,120,220,138,fill=gradiente('varillaDorada','varillaDoradaOScura')),
            Line(200,120,200,138,fill='varillaDoradaOscura'),
            Circle(208,128,5,fill=app.fondo),
            Circle(192,128,5,fill=app.fondo),
            Ovalo(200,120,7,10,fill='rosadoProfundo'),
            Star(201,116,4,4,fill='blanco')
            )
    
    #JAULA
    Rect(290,180,110,100,relleno=None,borde='plateado',anchuraDeBorde=5)
    Linea(320,180,320,280,relleno='plateado',anchuraDeLinea=5)
    Linea(370,180,370,280,relleno='plateado',anchuraDeLinea=5)
    Linea(345,180,345,280,relleno='plateado',anchuraDeLinea=5)
    
    #PRINCIPE
    Principe=Grupo(
            #brazos
            Ovalo(230,220,10,50,fill='white',rotarAngulo=-45),
            Ovalo(248,235,12,7,fill='marronArenoso'),
            Ovalo(166,230,10,50,fill='white',rotarAngulo=10),
            Ovalo(162,253,7,12,fill='marronArenoso'),
            #patas
            Linea(180,280,180,335,fill='white',anchuraDeLinea=18),
            Linea(210,280,210,335,fill='white',anchuraDeLinea=18),
            #torso
            Poligono(168,282,222,282,220,205,170,205,fill='white'),
            Linea(168,266,222,266,fill='rojo',anchuraDeLinea=10),
            Poligono(171,205,167,215,223,215,219,205,fill='gold'),
            Ovalo(195,205,50,10,fill='gold'),
            Linea(173,205,171,215),
            Linea(178,205,176,215),
            Linea(183,205,181,215),
            Linea(188,205,186,215),
            Linea(201,205,203,215),
            Linea(206,205,208,215),
            Linea(211,205,213,215),
            Linea(216,205,218,215),
            Linea(195,193,195,215,fill='white',anchuraDeLinea=10),
            Ovalo(195,205,8,12,fill='rojo'),
            Star(196,203,4,4,fill='blanco'),
            Circulo(195,181,15,fill='marronArenoso'),
            #pelo
            Ovalo(205,167,10,25,fill='marronCuero',rotarAngulo=-80),
            Ovalo(185,167,10,25,fill='marrónCuero',rotarAngulo=80),
            #cara
            Linea(192,173,183,176),
            Linea(198,173,208,176),
            Ovalo(190,180,3,5),
            Ovalo(200,180,3,5),
            Ovalo(195,190,4,7),
            #corona
            Poligono(170,168,195,140,220,168,fill=gradiente('varillaDorada','varillaDoradaOScura')),
            Linea(195,140,195,170,fill='varillaDoradaOscura'),
            Circulo(207,154,6,fill=app.fondo),
            Circulo(183,154,6,fill=app.fondo,opacity=70),
            Ovalo(195,140,9,11,fill='rojo'),
            Star(197,136,4,4,fill='blanco')
            )
    espada=Grupo(
            Rect(26,178,50,15,relleno='rojoNaranja',rotarAngulo=-52,borde='negro'),
            Linea(60,165,69,175),
            Linea(55,170,65,180),
            Linea(45,180,58,190),
            Circulo(40,200,10,relleno='varillaDoradaOscura',borde='negro'),
            Rect(48,155,40,20,rotarAngulo=35,relleno='varillaDoradaOscura',borde='negro'),
            Poligono(56,159,112,77,133,63,132,87,76,172,relleno=gradiente('gris','blanco','gris'),borde='negro'),
            Linea(67,165,133,63)
            )
    ### modificaciónes del dragón
    Dragon.altura = 200
    Dragon.ancho= 210
    Dragon.centroX = 100
    Dragon.centroY = 200
    ### modificaciónes de la luna
    Luna.altura = 100
    Luna.ancho = 100
    Luna.centroY = 60
    Luna.centroX = 200
    ### modificaciónes de la espada
    espada.altura=35
    espada.ancho=30
    espada.centroX=280
    espada.centroY=212
    espada.rotarAngulo=-15
    ### modificaciónes de la princesa
    Princesa.centroX=360
    Princesa.centroY=220
    Princesa.altura=100
    Princesa.ancho=85
    ### modificaciónes del principe 
    Principe.centroX=250
    Principe.centroY=230
    Principe.altura=100
    Principe.ancho=55

dibujarVictoria()
cmu_graphics.run()