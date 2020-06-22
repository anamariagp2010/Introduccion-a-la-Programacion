from tkinter import *
import time
import random


#Se crea la ventana principal con el nombre del juego y el tamaño 
ventana = Tk()
ventana.title("The Simpsons' Road")
ventana.geometry("900x500")
ventana.resizable(height=False ,width=False)

#Se coloca la imagen que saldra al comienzo del juego
start = PhotoImage(file="comienzo.PNG")
fondoStart = Label(ventana,image=start).place(x=0,y=0)

#se hace la función del boton de instrucciones
def instrucciones():
    ventanaIns = Toplevel()
    ventanaIns.geometry("700x400")
    ventanaIns.resizable(height=False ,width=False)
    #Se escribe lo que van a ir en las instrucciones
    ventanaIns.title("INSTRUCCIONES DEL JUEGO")
    titleInst=Label(ventanaIns,text = "INSTRUCCIONES DEL JUEGO \n \n")
    comoJugar = Label (ventanaIns,text = "¿CÓMO JUGAR? \n")
    inst1 = Label (ventanaIns,text = "- El jugador 1 usará las "
                       "teclas A y D para desplazarse \n a la izquierda y "
                       "derecha respectivamente.\n")
    inst2 = Label (ventanaIns,text = "- El jugador 2 usará las "
                       "flechas de DERECHA e IZQUIERDA para "
                       "desplazarse.\n"
                       "- No mantener la tecla presionada, pulsarla repetitivamente \n"
                       "- Presionar Tab para comenzar el juego \n"
                       "- Para pausar el juego, presione alt \n \n")
    reglasJuego = Label (ventanaIns,text = "REGLAS DEL JUEGO \n")
    inst3 = Label (ventanaIns,text = "- Se deben esquivar los carros que aparezcan")
    inst4 = Label (ventanaIns,text = "- No se puede salir de la pista")
    inst5 = Label (ventanaIns,text = "- No se debe pasar por los charcos de aceite")
    inst6 = Label (ventanaIns,text = "- Se deben tomar los depósitos de gasolina para tener más combustible")
    inst7 = Label (ventanaIns,text = "- Al iniciar el juego, se debe ingresar el nombre de los jugadores y escoger el nivel")
    inst8 = Label (ventanaIns,text = "- Se deben manejar los carros con el teclado")
    titleInst.pack()
    comoJugar.pack()
    inst1.pack()
    inst2.pack()
    reglasJuego.pack()
    inst3.pack()
    inst4.pack()
    inst5.pack()
    inst6.pack()
    inst7.pack()
    inst8.pack()

    #boton para salir de las instrucciones
    abandonarIns = Button(ventanaIns,text="SALIR",command=ventanaIns.destroy,bg="pink").place(x=595,y=320)

    
#imagenes que saldran en el nivel 1
pista1 = PhotoImage(file="level1.PNG")
pista2 = PhotoImage(file="level1.PNG")
bart = PhotoImage(file="bart.PNG")
rival1 = PhotoImage(file="rival11.PNG")
rival2 = PhotoImage(file="rival2.PNG")
rival3 = PhotoImage(file="rival3.PNG")
lisa = PhotoImage(file="lisa.PNG")
dona = PhotoImage(file="dona.png")
bartCara = PhotoImage(file="bartCara.png")

#contadores que se usaran en las funciones

#rival1
cRival1 = 0
segRival1 = 0
#rival2
cRival2x = 0
segRival2x = 0
cRival2y = 0
segRival2y = 0
#pistas 1 y 2
cPista1 = 0
cPista2 = 0
#donas
cDona1 = 0
cDona2 = 0


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# seguimiento posicion Bart y Lisa
posXBart = 250
posYBart = 600
posXLisa = 1000
posYLisa = 600


# Actualizacion de la posicion de la dona en x
def actualizarDona():
    global posXDona
    posXDona = random.randrange(180,390)

actualizarDona()

# Actualizacion de la posicion de la dona en x del segundo jugador
def actualizarDona2():
    global posXDona2
    posXDona2 = random.randrange(890,1110)

actualizarDona2()

# Posiciones en y de donas
posYDona = -200
posYDona2 = -200


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Actualizacion de la posicion en x del rival 1
def actualizarRival1():
    global posXRival1
    posXRival1 = random.randrange(180,390)

actualizarRival1()

# Actualizacion de la posicion en x del rival 1 del segundo jugador
def segActualizarRival1():
    global segPosXRival1
    segPosXRival1 = random.randrange(890,1110)

segActualizarRival1()

# posicion en y del rival 1
posYRival1 = -400
segPosYRival1 = -400


# Actualizacion de la posicion en x del rival 1

posXRival2 = 120
segPosXRival2 = 850

posYRival2 = 0
segPosYRival2 = 0

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Actualizacion de la posicion en x del rival 3
def actualizarRival3():
    global posXRival3
    posXRival3 = random.randrange(180,390)
    
actualizarRival3()


# Actualizacion de la posicion en x del rival 3 del segundo jugador
def segActualizarRival3():
    global segPosXRival3
    segPosXRival3 = random.randrange(890,1110)
    
segActualizarRival3()

# posicion en y del rival 3
segPosYRival3 = -300
posYRival3 = -300



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Función del nivel 1
def nivel1():
    global ventana1, canvas1,imagenPista1, ventanaMenu, imagenRival1, imagenRival2, dona, imagenDona2, posXDona, posYDona
    global imagenPista2, imagenBart, segImagenRival1, segImagenRival2, contGas, contGas2, imagenDona, cDona, posYBart 
    global posYLisa, posXLisa, posXDona2, posYDona2, posXBart, posYRival1,segPosYRival1,posXRival1,segPosXRival1
    global posXRival3,posYRival3,contXRival3,imagenRival3,segImagenRival3,segPosXRival3,segPosYRival3,segContXRival3
    global segPosXRival2,segPosYRival2,labelPuntos,contPuntos,labelPuntos2,contPuntos2,vr1,vr2
     
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #al abrir el nivel uno, se minimiza la ventana del menu
    ventanaMenu.iconify()
    ventana1 = Toplevel()
    ventana1.title("NIVEL UNO")
    
    #canvas nivel 1
    canvas1 = Canvas(ventana1, width = 1920, height = 1080, bg="black")
    canvas1.pack()
    
    #Se crean las imagenes en el canvas

    #imagenes de las pistas
    imagenPista1 = canvas1.create_image(270,-14200,image = pista1)
    imagenPista2 = canvas1.create_image(1012,-14200,image = pista1)

    #imagenes de los jugadores
    imagenBart = canvas1.create_image(posXBart,posYBart,image = bart)
    imagenLisa = canvas1.create_image(posXLisa,posYLisa,image = lisa)

    #rival 1
    imagenRival1 = canvas1.create_image(posXRival1,posYRival1,image = rival1)
    segImagenRival1 = canvas1.create_image(segPosXRival1,segPosYRival1,image = rival1)
    #rival 2    
    imagenRival2 = canvas1.create_image(posXRival2,posYRival2,image = rival2)
    segImagenRival2 = canvas1.create_image(segPosXRival2,segPosYRival2,image = rival2)
    #rival 3
    imagenRival3 = canvas1.create_image(posXRival3,posYRival3,image = rival3)
    segImagenRival3 = canvas1.create_image(segPosXRival3,segPosYRival3,image = rival3)

    #otras imagenes
    imagenDona = canvas1.create_image(posXDona,posYDona,image = dona)
    imagenDona2 = canvas1.create_image(posXDona2,posYDona2,image = dona)
    #imagenBartCara = canvas1.create_image(180,600,image = bartCara)
    
    #Se coloca el nombre de los jugadores en la pantalla
    jugador1 = Label(canvas1, text = "Jugador 1 : \n" + vr1.get()).place(x=410,y=50)                
    jugador2 = Label(canvas1, text = "Jugador 2 : \n" + vr2.get()).place(x=1150,y=50)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Se crea la funcion para devolver al menu, que cierra la partida y abre el menu
    def volverMenu1():
        ventana1.destroy()
        ventanaMenu.deiconify()

    #Se hace el boton de volver al menu
    volverMenu = Button(ventana1,text="Regresar Al Menú",command=volverMenu1,bg="yellow").place(x=590,y=580)

    def siguienteNivel1():
        ventana1.destroy()
        nivel2()

    siguienteNivel = Button(ventana1,text="Siguiente Nivel",command=siguienteNivel1,bg="yellow").place(x=595,y=400)    

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # funcion del movimiento del rival 1 (carro que va en un solo carril)
    def moveRival1():
        global canvas1, ventana1, rival1, cRival1, imagenRival1, posYRival1,contGas,posXBart,posYBart

        # Mueve al carro solo en y
        if(cRival1 < 220):
            canvas1.move(imagenRival1,0,5)
            cRival1 += 1
            posYRival1 += 5

            #se crea el choque de Bart con el rival 1
            if(posXBart >= posXRival1 -37 and posXBart <= posXRival1 +37 and posYBart >= posYRival1 -76 and posYBart <= posYRival1 +76):
                contGas -= 3
                canvas1.delete(imagenRival1)
                posYRival1 = -400
            canvas1.after(40,moveRival1)

        # Cuando se termina la pista, se repite el proceso
        else:
            cRival1 = 0
            canvas1.delete(imagenRival1)
            posYRival1 = -400
            actualizarRival1()
            imagenRival1 = canvas1.create_image(posXRival1,posYRival1,image = rival1)
            moveRival1()



    #funcion del rival uno para el segundo jugador
    def segMoveRival1():
        global canvas1, ventana1, rival1, segRival1, segImagenRival1,segPosXRival1,segPosYRival1,contGas2

        # Mueve al carro solo en y
        if(segRival1 < 220):
            canvas1.move(segImagenRival1,0,5)
            segRival1 += 1
            segPosYRival1 += 5

            #se crea el choque de Lisa con el rival 1
            if(posXLisa >= segPosXRival1 -37 and posXLisa <= segPosXRival1 +37 and posYLisa >= segPosYRival1 -76 and posYLisa <= segPosYRival1 +76):
                contGas2 -= 3
                canvas1.delete(segImagenRival1)
                segPosYRival1 = -400
            canvas1.after(40,segMoveRival1)

        # Cuando se termina la pista, se repite el proceso
        else:
            segRival1 = 0
            canvas1.delete(segImagenRival1)
            segPosYRival1 = -400
            segActualizarRival1()
            segImagenRival1 = canvas1.create_image(segPosXRival1,segPosYRival1,image = rival1) 
            segMoveRival1()


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Movimiento del rival 2 (Carro que cambia de carril)
    def moveRival2():
        global canvas1, ventana1, rival2, cRival2x, imagenRival2, cRival2y,posXRival2,posYRival2, contGas

        #Se mueve diagonalmente hacia la derecha
        if (cRival2x < 53):
            canvas1.move(imagenRival2,5,3)
            cRival2x += 1
            posXRival2 += 5
            posYRival2 += 3
            
         
            if(posXBart >= posXRival2 -60 and posXBart <= posXRival2 +60 and posYBart >= posYRival2 -39 and posYBart <= posYRival2 +39):
                canvas1.delete(imagenRival2)
                contGas -= 3
                posYRival2 = 0
                
                
            canvas1.after(40,moveRival2)    
        # Al chocar con el borde de la carretera, comienza el movimiento diagonal hacia la izquierda
        elif (cRival2x >= 53 and cRival2x < 104):
            canvas1.move(imagenRival2,-5,3)
            cRival2x += 1
            cRival2y += 1
            posXRival2 -= 5
            posYRival2 += 3

            if(posXBart >= posXRival2 -60 and posXBart <= posXRival2 +60 and posYBart >= posYRival2 -39 and posYBart <= posYRival2+39):
                canvas1.delete(imagenRival2)
                contGas -= 3
                posYRival2 = 0
                
            
            
            # Cuando llegue al final de la carretera, se borra la imagen y se crea de nuevo para volver a comenzar
            if(cRival2y >= random.randrange(120,200)):
                cRival2x = 0
                cRival2y = 0
                posXRival2 = 120
                posYRival2 = 0
                canvas1.delete(imagenRival2)
                imagenRival2 = canvas1.create_image(120,-50,image = rival2)
            canvas1.after(40,moveRival2)

        # Llama de nuevo a la funcion para que se repitan los condicionales anteriores
        else:        
            cRival2x = 0
            moveRival2()



    #movimiento del rival 2 para el 2do jugador
    def segMoveRival2():
        global canvas1, ventana1, rival2, segRival2x, segImagenRival2, segRival2y,segPosYRival2,segPosXRival2,contGas2

        #Se mueve diagonalmente hacia la derecha
        if (segRival2x < 53):
            canvas1.move(segImagenRival2,5,3)
            segRival2x += 1
            segPosXRival2 += 5
            segPosYRival2 += 3

            if(posXLisa >= segPosXRival2 -60 and posXLisa <= segPosXRival2 +60 and posYLisa >= segPosYRival2 -39 and posYLisa <= segPosYRival2 +39):
                canvas1.delete(segImagenRival2)
                contGas2 -= 3
                segPosYRival2 = 0
                

            canvas1.after(40,segMoveRival2)   
            
        # Al chocar con el borde de la carretera, comienza el movimiento diagonal
        # hacia la izquierda
        elif (segRival2x >= 53 and segRival2x < 104):
            canvas1.move(segImagenRival2,-5,3)
            segRival2x += 1
            segRival2y += 1
            segPosXRival2 -= 5
            segPosYRival2 += 3

            if(posXLisa >= segPosXRival2 -60 and posXLisa <= segPosXRival2 +60 and posYLisa >= segPosYRival2 -39 and posYLisa <= segPosYRival2 +39):
                canvas1.delete(segImagenRival2)
                contGas2 -= 3
                segPosYRival2 = 0
                
            
            # Cuando llegue al final de la carretera, se borra la imagen y se crea de nuevo para volver a comenzar
            if(segRival2y >= random.randrange(120,200)):
                segRival2x = 0
                segRival2y = 0
                segPosXRival2 = 850
                segPosYRival2 = 0
                canvas1.delete(segImagenRival2)
                segImagenRival2 = canvas1.create_image(850,-50,image = rival2)

            canvas1.after(40,segMoveRival2)   

        # Llama de nuevo a la funcion para que se repitan los condicionales anteriores
        else:        
            segRival2x = 0
            segMoveRival2()


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # funcion del movimiento del rival 3 (carro que persigue al jugador)
    contXRival3 = 0
    def moveRival3():
        global posYRival3,posXRival3, contXRival3,imagenRival3, contGas

        # condicional mientras se mueve por la pista 
        if(contXRival3 < 180):
            
            if(posXRival3 < posXBart):
                canvas1.move(imagenRival3,0.8,5)
                posXRival3 += 0.8
                posYRival3 += 5
            elif(posXRival3 > posXBart):
                canvas1.move(imagenRival3,-0.8,5)
                posXRival3 -= 0.8
                posYRival3 += 5
            else:
                canvas1.move(imagenRival3,0,5)
                posYRival3 += 5


            if(posXBart >= posXRival3 -45 and posXBart <= posXRival3 +45 and posYBart >= posYRival3 -72 and posYBart <= posYRival3 +72):
                canvas1.delete(imagenRival3)
                contGas -= 3
                posYRival3 = 0
            

            contXRival3 += 1
            canvas1.after(50,moveRival3)

        #condicional al terminar la pista para recomenzar
        else:
            posYRival3 = 0
            contXRival3 = -300
            actualizarRival3()
            canvas1.delete(imagenRival3)
            imagenRival3 = canvas1.create_image(posXRival3,posYRival3,image = rival3)
            moveRival3()



    # funcion del movimiento del rival 3 (carro que persigue al jugador) del segundo jugador
    segContXRival3 = 0
    def segMoveRival3():
        global segPosYRival3,segPosXRival3, segContXRival3,segImagenRival3,contGas2

        # condicional mientras se mueve por la pista del segundo jugador
        if(segContXRival3 < 180):
            if(segPosXRival3 < posXLisa):
                canvas1.move(segImagenRival3,0.8,5)
                segPosXRival3 += 0.8
                segPosYRival3 += 5
            elif(segPosXRival3 > posXLisa):
                canvas1.move(segImagenRival3,-0.8,5)
                segPosXRival3 -= 0.8
                segPosYRival3 += 5
            else:
                canvas1.move(segImagenRival3,0,5)
                segPosYRival3 += 5

            if(posXLisa >= segPosXRival3 -45 and posXLisa <= segPosXRival3 +45 and posXLisa >= segPosYRival3 -72 and posXLisa <= segPosYRival3 +72):
                canvas1.delete(segImagenRival3)
                segPosYRival3 = 0
                contGas2 -= 3
                

            segContXRival3 += 1
            canvas1.after(50,segMoveRival3)

        #condicional al terminar la pista para recomenzar del segundo jugador
        else:
            segPosYRival3 = 0
            segContXRival3 = -300
            segActualizarRival3()
            canvas1.delete(segImagenRival3)
            segImagenRival3 = canvas1.create_image(segPosXRival3,segPosYRival3,image = rival3)
            segMoveRival3()



    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Se hace el movimiento del jugador uno (Bart)
    def moveBart(event):
        global posXBart
        
        #condicional para los limites del lado izquierdo
        if (canvas1.coords(imagenBart) == [130,600]):
            canvas1.move(imagenBart,0,0)
            #canvas1.delete(imagenBart)
            #magenBartCara = canvas1.create_image(145,600,image = bartCara)
            
            
        elif (event.keysym == 'a' or event.keysym == 'A'):
            canvas1.move(imagenBart,-10,0)
            posXBart-=10
            

        #condicional para los limites del lado derecho          
        if (canvas1.coords(imagenBart) == [370,600]):
            canvas1.move(imagenBart,0,0)
            #canvas1.delete(imagenBart)
            #imagenBartCara = canvas1.create_image(380,600,image = bartCara)
    
        elif (event.keysym == 'd' or event.keysym == 'D'):
            canvas1.move(imagenBart,10,0)
            posXBart+=10


    """"""
    # movimiento del jugador 2 (Lisa)
    def moveLisa(event):
        global posXLisa

        #condicional para los limites del lado izquierdo
        if (canvas1.coords(imagenLisa) == [880,600]):
            canvas1.move(imagenLisa,0,0)
            
        elif (event.keysym == "Left"):
            canvas1.move(imagenLisa,-10,0)
            posXLisa -= 10

        #condicional para los limites del lado derecho          
        if (canvas1.coords(imagenLisa) == [1120,600]):
            canvas1.move(imagenLisa,0,0)
    
        elif (event.keysym == "Right"):
            canvas1.move(imagenLisa,10,0)
            posXLisa += 10

      
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Se hace el movimiento de la pista 1
    def movePista1():
        global cPista1,contPuntos,contPuntos2
        if (cPista1<1800):
            canvas1.move(imagenPista1,0,15)
            cPista1 +=1
            canvas1.after(50,movePista1)
        elif(cPista1==1800):
            if (contPuntos > contPuntos2):
                ganador = Label(canvas1,text="EL GANADOR ES \n "+vr1.get(),height=8,width=20).place(x=577,y=170)
            elif (contPuntos2 > contPuntos):
                ganador = Label(canvas1,text="EL GANADOR ES \n "+vr2.get(),height=8,width=20).place(x=577,y=170)
            else:
                ganador = Label(canvas1,text="¡ HA HABIDO UN EMPATE !",height=5,width=20).place(x=577,y=170)
                

    #Se hace el movimiento de la pista 2
    def movePista2():
        global cPista2
        if (cPista2<1800):
            canvas1.move(imagenPista2,0,15)
            cPista2 +=1
            canvas1.after(50,movePista2)
        elif(cPista2==1800):
            if (contPuntos > contPuntos2):
                ganador = Label(canvas1,text="EL GANADOR ES \n "+vr1.get(),height=8,width=20).place(x=577,y=170)
            elif (contPuntos2 > contPuntos):
                ganador = Label(canvas1,text="EL GANADOR ES \n "+vr2.get(),height=8,width=20).place(x=577,y=170)
            else:
                ganador = Label(canvas1,text="¡ HA HABIDO UN EMPATE !",height=5,width=20).place(x=577,y=170)



    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Funcion de la gasolina del jugador uno
    contGas = 100
    def gasolina1():
        global labelGas, contGas, canvas1,cPista1
        # Se crea el label donde se va a mostrar la gasolina
        labelGas = Label(ventana1)
        labelGas.config(text = "Energía : \n"+str(contGas))
        labelGas.place(x=415,y=150)
        if(contGas>0):
            contGas = contGas-1
            canvas1.after(1000,gasolina1)
        else:
            cPista1 = 1900
            
        

    # Funcion de la gasolina del jugador uno
    contGas2 = 100
    def gasolina2():
        global labelGas2, contGas2, canvas1
        # Se crea el label donde se va a mostrar la gasolina
        labelGas2 = Label(ventana1)
        labelGas2.config(text = "Energía : \n"+str(contGas2))
        labelGas2.place(x=1155,y=150)
        if(contGas2>0):
            contGas2 = contGas2 -1
            canvas1.after(1000,gasolina2)
        else:
            cPista2 = 1900
            
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    contPuntos = 0
    def puntos():
        global labelPuntos,contPuntos,contGas
        labelPuntos = Label(ventana1)
        labelPuntos.config(text = "1P \n"+str(contPuntos))
        labelPuntos.place(x=415,y=250)
        if(contPuntos>=0):
            if(contGas>0):
                contPuntos += 50
            canvas1.after(1000,puntos)

    contPuntos2 = 0
    def puntos2():
        global labelPuntos2,contPuntos2,contGas2
        labelPuntos2 = Label(ventana1)
        labelPuntos2.config(text = "2P \n"+str(contPuntos2))
        labelPuntos2.place(x=1155,y=250)
        if(contPuntos2>=0):
            if(contGas2>0):
                contPuntos2 += 50
            canvas1.after(1000,puntos2)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def funDona1():
        global contGas, canvas1, ventana1, dona, cDona1, imagenDona, posXBart, posXDona, posYDona, posYBart,contPuntos
        
        # Mueve al carro solo en y
        if(cDona1 < 220):
            canvas1.move(imagenDona,0,5)
            cDona1 += 1
            posYDona +=5

            if(posXBart >= posXDona-40 and posXBart <= posXDona+40 and posYBart >= posYDona-40 and posYBart <= posYDona+40):
                if(contGas>0):
                    contGas+=7
                    contPuntos += 1000
                posYDona = -200
                canvas1.delete(imagenDona)
            canvas1.after(40,funDona1)

        # Cuando se termina la pista, se repite el proceso
        else:
            cDona1 = 0
            canvas1.delete(imagenDona)
            posYDona = -200
            actualizarDona()
            imagenDona = canvas1.create_image(posXDona,posYDona,image = dona)  
            funDona1()



    def funDona2():
        global contGas2, canvas1, ventana1, dona, cDona2, imagenDona2, posXLisa, posXDona2, posYDona2, posYLisa,contPuntos2
        
        # Mueve al carro solo en y
        if(cDona2 < 220):
            canvas1.move(imagenDona2,0,5)
            cDona2 += 1
            posYDona2 += 5

            if(posXLisa >= posXDona2 -40 and posXLisa <= posXDona2 +40 and posYLisa >= posYDona2-40 and posYLisa <= posYDona2+40):
                if(contGas2>0):
                    contGas2 += 7
                    contPuntos2 += 1000
                posYDona2 = -200
                canvas1.delete(imagenDona2)
            canvas1.after(40,funDona2)
            
        # Cuando se termina la pista, se repite el proceso
        else:
            cDona2 = 0
            canvas1.delete(imagenDona2)
            posYDona2 = -200
            actualizarDona2()
            imagenDona2 = canvas1.create_image(posXDona2,posYDona2,image = dona)  
            funDona2()

        
            
            

    def iniciar(event):
        if (event.keysym == 'Tab'):
            moveRival1()
            segMoveRival1()
            moveRival2()
            segMoveRival2()
            moveRival3()
            segMoveRival3()
            canvas1.bind_all("<KeyPress-a>", moveBart)
            canvas1.bind_all("<KeyPress-A>", moveBart)
            canvas1.bind_all("<KeyPress-d>", moveBart)
            canvas1.bind_all("<KeyPress-D>", moveBart)
            canvas1.bind_all("<KeyPress-Left>", moveLisa)
            canvas1.bind_all("<KeyPress-Right>", moveLisa)
            movePista1()
            movePista2()
            gasolina1()
            gasolina2()
            funDona1()
            funDona2()
            puntos()
            puntos2()
            
            
    
    canvas1.bind_all("<KeyPress-Tab>", iniciar)

    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Función del nivel 2

#imagenes que saldran en el nivel 1
nvl2pista1 = PhotoImage(file="level1.PNG")
nvl2pista2 = PhotoImage(file="level1.PNG")
nvl2bart = PhotoImage(file="bart.PNG")
nvl2rival1 = PhotoImage(file="rival11.PNG")
nvl2rival2 = PhotoImage(file="rival2.PNG")
nvl2rival3 = PhotoImage(file="rival3.PNG")
nvl2lisa = PhotoImage(file="lisa.PNG")
nvl2dona = PhotoImage(file="dona.png")

#contadores que se usaran en las funciones

#nvl2rival1
nvl2cnvl2rival1 = 0
segnvl2rival1 = 0
#nvl2rival2
cnvl2rival2x = 0
segnvl2rival2x = 0
cnvl2rival2y = 0
segnvl2rival2y = 0
#pistas 1 y 2
cnvl2pista1 = 0
cnvl2pista2 = 0
#nvl2donas
cnvl2dona1 = 0
cnvl2dona2 = 0


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# seguimiento posicion nvl2bart y nvl2lisa
posXnvl2bart = 250
posYnvl2bart = 600
posXnvl2lisa = 1000
posYnvl2lisa = 600


# Actualizacion de la posicion de la nvl2dona en x
def actualizarnvl2dona():
    global posXnvl2dona
    posXnvl2dona = random.randrange(180,390)

actualizarnvl2dona()

# Actualizacion de la posicion de la nvl2dona en x del segundo jugador
def actualizarnvl2dona2():
    global posXnvl2dona2
    posXnvl2dona2 = random.randrange(890,1110)

actualizarnvl2dona2()

# Posiciones en y de nvl2donas
posYnvl2dona = -200
posYnvl2dona2 = -200


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Actualizacion de la posicion en x del rival 1
def actualizarnvl2rival1():
    global posXnvl2rival1
    posXnvl2rival1 = random.randrange(180,390)

actualizarnvl2rival1()

# Actualizacion de la posicion en x del rival 1 del segundo jugador
def segActualizarnvl2rival1():
    global segPosXnvl2rival1
    segPosXnvl2rival1 = random.randrange(890,1110)

segActualizarnvl2rival1()

# posicion en y del rival 1
posYnvl2rival1 = -400
segPosYnvl2rival1 = -400


# Actualizacion de la posicion en x del rival 1

posXnvl2rival2 = 120
segPosXnvl2rival2 = 850

posYnvl2rival2 = 0
segPosYnvl2rival2 = 0

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Actualizacion de la posicion en x del rival 3
def actualizarnvl2rival3():
    global posXnvl2rival3
    posXnvl2rival3 = random.randrange(180,390)
    
actualizarnvl2rival3()


# Actualizacion de la posicion en x del rival 3 del segundo jugador
def segActualizarnvl2rival3():
    global segPosXnvl2rival3
    segPosXnvl2rival3 = random.randrange(890,1110)
    
segActualizarnvl2rival3()

# posicion en y del rival 3
segPosYnvl2rival3 = -300
posYnvl2rival3 = -300



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Función del nivel 1
def nivel2():
    global ventana2, canvas2,imagennvl2pista1, ventanaMenu, imagennvl2rival1, imagennvl2rival2, nvl2dona, imagennvl2dona2, posXnvl2dona, posYnvl2dona
    global imagennvl2pista2, imagennvl2bart, segImagennvl2rival1, segImagennvl2rival2, nvl2contGas, nvl2contGas2, imagennvl2dona, cnvl2dona, posYnvl2bart 
    global posYnvl2lisa, posXnvl2lisa, posXnvl2dona2, posYnvl2dona2, posXnvl2bart, posYnvl2rival1,segPosYnvl2rival1,posXnvl2rival1,segPosXnvl2rival1
    global posXnvl2rival3,posYnvl2rival3,contXnvl2rival3,imagennvl2rival3,segImagennvl2rival3,segPosXnvl2rival3,segPosYnvl2rival3,segContXnvl2rival3
    global segPosXnvl2rival2,segPosYnvl2rival2,nvl2labelnvl2puntos,nvl2contnvl2puntos,nvl2labelnvl2puntos2,nvl2contnvl2puntos2,vr1,vr2
     
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #al abrir el nivel uno, se minimiza la ventana del menu
    ventanaMenu.iconify()
    ventana2 = Toplevel()
    ventana2.title("NIVEL DOS")
    
    #canvas nivel 1
    canvas2 = Canvas(ventana2, width = 1920, height = 1080, bg="black")
    canvas2.pack()
    
    #Se crean las imagenes en el canvas

    #imagenes de las pistas
    imagennvl2pista1 = canvas2.create_image(270,-14200,image = nvl2pista1)
    imagennvl2pista2 = canvas2.create_image(1012,-14200,image = nvl2pista1)

    #imagenes de los jugadores
    imagennvl2bart = canvas2.create_image(posXnvl2bart,posYnvl2bart,image = nvl2bart)
    imagennvl2lisa = canvas2.create_image(posXnvl2lisa,posYnvl2lisa,image = nvl2lisa)

    #rival 1
    imagennvl2rival1 = canvas2.create_image(posXnvl2rival1,posYnvl2rival1,image = nvl2rival1)
    segImagennvl2rival1 = canvas2.create_image(segPosXnvl2rival1,segPosYnvl2rival1,image = nvl2rival1)
    #rival 2    
    imagennvl2rival2 = canvas2.create_image(posXnvl2rival2,posYnvl2rival2,image = nvl2rival2)
    segImagennvl2rival2 = canvas2.create_image(segPosXnvl2rival2,segPosYnvl2rival2,image = nvl2rival2)
    #rival 3
    imagennvl2rival3 = canvas2.create_image(posXnvl2rival3,posYnvl2rival3,image = nvl2rival3)
    segImagennvl2rival3 = canvas2.create_image(segPosXnvl2rival3,segPosYnvl2rival3,image = nvl2rival3)

    #otras imagenes
    imagennvl2dona = canvas2.create_image(posXnvl2dona,posYnvl2dona,image = nvl2dona)
    imagennvl2dona2 = canvas2.create_image(posXnvl2dona2,posYnvl2dona2,image = nvl2dona)
    #imagennvl2bartCara = canvas2.create_image(180,600,image = nvl2bartCara)
    
    #Se coloca el nombre de los jugadores en la pantalla
    nvl2jugador1 = Label(canvas2, text = "Jugador 1 : \n" + vr1.get()).place(x=410,y=50)                
    nvl2jugador2 = Label(canvas2, text = "Jugador 2 : \n" + vr2.get()).place(x=1150,y=50)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Se crea la funcion para devolver al menu, que cierra la partida y abre el menu
    def nvl2nvl2volverMenu1():
        ventana2.destroy()
        ventanaMenu.deiconify()

    #Se hace el boton de volver al menu
    nvl2volverMenu = Button(ventana2,text="Regresar Al Menú",command=nvl2nvl2volverMenu1,bg="yellow").place(x=590,y=580)

    def nvl2siguientenivel2():
        ventana2.destroy()
        nivel3()

    nvl2siguienteNivel = Button(ventana2,text="Siguiente Nivel",command=nvl2siguientenivel2,bg="yellow").place(x=595,y=400)    

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # funcion del movimiento del rival 1 (carro que va en un solo carril)
    def movenvl2rival1():
        global canvas2, ventana2, nvl2rival1, nvl2cnvl2rival1, imagennvl2rival1, posYnvl2rival1,nvl2contGas,posXnvl2bart,posYnvl2bart

        # Mueve al carro solo en y
        if(nvl2cnvl2rival1 < 220):
            canvas2.move(imagennvl2rival1,0,6)
            nvl2cnvl2rival1 += 1
            posYnvl2rival1 += 6

            #se crea el choque de nvl2bart con el rival 1
            if(posXnvl2bart >= posXnvl2rival1 -37 and posXnvl2bart <= posXnvl2rival1 +37 and posYnvl2bart >= posYnvl2rival1 -76 and posYnvl2bart <= posYnvl2rival1 +76):
                nvl2contGas -= 3
                canvas2.delete(imagennvl2rival1)
                posYnvl2rival1 = -400
            canvas2.after(40,movenvl2rival1)

        # Cuando se termina la pista, se repite el proceso
        else:
            nvl2cnvl2rival1 = 0
            canvas2.delete(imagennvl2rival1)
            posYnvl2rival1 = -400
            actualizarnvl2rival1()
            imagennvl2rival1 = canvas2.create_image(posXnvl2rival1,posYnvl2rival1,image = nvl2rival1)
            movenvl2rival1()



    #funcion del rival uno para el segundo jugador
    def segMovenvl2rival1():
        global canvas2, ventana2, nvl2rival1, segnvl2rival1, segImagennvl2rival1,segPosXnvl2rival1,segPosYnvl2rival1,nvl2contGas2

        # Mueve al carro solo en y
        if(segnvl2rival1 < 220):
            canvas2.move(segImagennvl2rival1,0,6)
            segnvl2rival1 += 1
            segPosYnvl2rival1 += 6

            #se crea el choque de nvl2lisa con el rival 1
            if(posXnvl2lisa >= segPosXnvl2rival1 -37 and posXnvl2lisa <= segPosXnvl2rival1 +37 and posYnvl2lisa >= segPosYnvl2rival1 -76 and posYnvl2lisa <= segPosYnvl2rival1 +76):
                nvl2contGas2 -= 3
                canvas2.delete(segImagennvl2rival1)
                segPosYnvl2rival1 = -400
            canvas2.after(40,segMovenvl2rival1)

        # Cuando se termina la pista, se repite el proceso
        else:
            segnvl2rival1 = 0
            canvas2.delete(segImagennvl2rival1)
            segPosYnvl2rival1 = -400
            segActualizarnvl2rival1()
            segImagennvl2rival1 = canvas2.create_image(segPosXnvl2rival1,segPosYnvl2rival1,image = nvl2rival1) 
            segMovenvl2rival1()


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Movimiento del rival 2 (Carro que cambia de carril)
    def movenvl2rival2():
        global canvas2, ventana2, nvl2rival2, cnvl2rival2x, imagennvl2rival2, cnvl2rival2y,posXnvl2rival2,posYnvl2rival2, nvl2contGas

        #Se mueve diagonalmente hacia la derecha
        if (cnvl2rival2x < 53):
            canvas2.move(imagennvl2rival2,6,4)
            cnvl2rival2x += 1
            posXnvl2rival2 += 6
            posYnvl2rival2 += 4

            if(posXnvl2bart >= posXnvl2rival2 -60 and posXnvl2bart <= posXnvl2rival2 +60 and posYnvl2bart >= posYnvl2rival2 -39 and posYnvl2bart <= posYnvl2rival2 +39):
                canvas2.delete(imagennvl2rival2)
                nvl2contGas -= 3
                posYnvl2rival2 = 0
                
                
            canvas2.after(40,movenvl2rival2)    
        # Al chocar con el borde de la carretera, comienza el movimiento diagonal hacia la izquierda
        elif (cnvl2rival2x >= 53 and cnvl2rival2x < 104):
            canvas2.move(imagennvl2rival2,-6,4)
            cnvl2rival2x += 1
            cnvl2rival2y += 1
            posXnvl2rival2 -= 6
            posYnvl2rival2 += 4

            if(posXnvl2bart >= posXnvl2rival2 -60 and posXnvl2bart <= posXnvl2rival2 +60 and posYnvl2bart >= posYnvl2rival2 -39 and posYnvl2bart <= posYnvl2rival2+39):
                canvas2.delete(imagennvl2rival2)
                nvl2contGas -= 3
                posYnvl2rival2 = 0
                
            
            
            # Cuando llegue al final de la carretera, se borra la imagen y se crea de nuevo para volver a comenzar
            if(cnvl2rival2y >= random.randrange(120,200)):
                cnvl2rival2x = 0
                cnvl2rival2y = 0
                posXnvl2rival2 = 120
                posYnvl2rival2 = 0
                canvas2.delete(imagennvl2rival2)
                imagennvl2rival2 = canvas2.create_image(120,-50,image = nvl2rival2)
            canvas2.after(40,movenvl2rival2)

        # Llama de nuevo a la funcion para que se repitan los condicionales anteriores
        else:        
            cnvl2rival2x = 0
            movenvl2rival2()



    #movimiento del rival 2 para el 2do jugador
    def segMovenvl2rival2():
        global canvas2, ventana2, nvl2rival2, segnvl2rival2x, segImagennvl2rival2, segnvl2rival2y,segPosYnvl2rival2,segPosXnvl2rival2,nvl2contGas2

        #Se mueve diagonalmente hacia la derecha
        if (segnvl2rival2x < 53):
            canvas2.move(segImagennvl2rival2,6,4)
            segnvl2rival2x += 1
            segPosXnvl2rival2 += 6
            segPosYnvl2rival2 += 4

            if(posXnvl2lisa >= segPosXnvl2rival2 -60 and posXnvl2lisa <= segPosXnvl2rival2 +60 and posYnvl2lisa >= segPosYnvl2rival2 -39 and posYnvl2lisa <= segPosYnvl2rival2 +39):
                canvas2.delete(segImagennvl2rival2)
                nvl2contGas2 -= 3
                segPosYnvl2rival2 = 0
                

            canvas2.after(40,segMovenvl2rival2)   
            
        # Al chocar con el borde de la carretera, comienza el movimiento diagonal
        # hacia la izquierda
        elif (segnvl2rival2x >= 53 and segnvl2rival2x < 104):
            canvas2.move(segImagennvl2rival2,-6,4)
            segnvl2rival2x += 1
            segnvl2rival2y += 1
            segPosXnvl2rival2 -= 6
            segPosYnvl2rival2 += 4

            if(posXnvl2lisa >= segPosXnvl2rival2 -60 and posXnvl2lisa <= segPosXnvl2rival2 +60 and posYnvl2lisa >= segPosYnvl2rival2 -39 and posYnvl2lisa <= segPosYnvl2rival2 +39):
                canvas2.delete(segImagennvl2rival2)
                nvl2contGas2 -= 3
                segPosYnvl2rival2 = 0
                
            
            # Cuando llegue al final de la carretera, se borra la imagen y se crea de nuevo para volver a comenzar
            if(segnvl2rival2y >= random.randrange(120,200)):
                segnvl2rival2x = 0
                segnvl2rival2y = 0
                segPosXnvl2rival2 = 850
                segPosYnvl2rival2 = 0
                canvas2.delete(segImagennvl2rival2)
                segImagennvl2rival2 = canvas2.create_image(850,-50,image = nvl2rival2)

            canvas2.after(40,segMovenvl2rival2)   

        # Llama de nuevo a la funcion para que se repitan los condicionales anteriores
        else:        
            segnvl2rival2x = 0
            segMovenvl2rival2()


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # funcion del movimiento del rival 3 (carro que persigue al jugador)
    contXnvl2rival3 = 0
    def movenvl2rival3():
        global posYnvl2rival3,posXnvl2rival3, contXnvl2rival3,imagennvl2rival3, nvl2contGas

        # condicional mientras se mueve por la pista 
        if(contXnvl2rival3 < 180):
            
            if(posXnvl2rival3 < posXnvl2bart):
                canvas2.move(imagennvl2rival3,1.5,6)
                posXnvl2rival3 += 1.5
                posYnvl2rival3 += 6
            elif(posXnvl2rival3 > posXnvl2bart):
                canvas2.move(imagennvl2rival3,-1.5,6)
                posXnvl2rival3 -= 1.5
                posYnvl2rival3 += 6
            else:
                canvas2.move(imagennvl2rival3,0,5)
                posYnvl2rival3 += 6


            if(posXnvl2bart >= posXnvl2rival3 -45 and posXnvl2bart <= posXnvl2rival3 +45 and posYnvl2bart >= posYnvl2rival3 -72 and posYnvl2bart <= posYnvl2rival3 +72):
                canvas2.delete(imagennvl2rival3)
                nvl2contGas -= 3
                posYnvl2rival3 = 0
            

            contXnvl2rival3 += 1
            canvas2.after(50,movenvl2rival3)

        #condicional al terminar la pista para recomenzar
        else:
            posYnvl2rival3 = 0
            contXnvl2rival3 = -300
            actualizarnvl2rival3()
            canvas2.delete(imagennvl2rival3)
            imagennvl2rival3 = canvas2.create_image(posXnvl2rival3,posYnvl2rival3,image = nvl2rival3)
            movenvl2rival3()



    # funcion del movimiento del rival 3 (carro que persigue al jugador) del segundo jugador
    segContXnvl2rival3 = 0
    def segMovenvl2rival3():
        global segPosYnvl2rival3,segPosXnvl2rival3, segContXnvl2rival3,segImagennvl2rival3,nvl2contGas2

        # condicional mientras se mueve por la pista del segundo jugador
        if(segContXnvl2rival3 < 180):
            if(segPosXnvl2rival3 < posXnvl2lisa):
                canvas2.move(segImagennvl2rival3,1.5,6)
                segPosXnvl2rival3 += 1.5
                segPosYnvl2rival3 += 6
            elif(segPosXnvl2rival3 > posXnvl2lisa):
                canvas2.move(segImagennvl2rival3,-1.5,6)
                segPosXnvl2rival3 -= 1.5
                segPosYnvl2rival3 += 6
            else:
                canvas2.move(segImagennvl2rival3,0,6)
                segPosYnvl2rival3 += 6

            if(posXnvl2lisa >= segPosXnvl2rival3 -45 and posXnvl2lisa <= segPosXnvl2rival3 +45 and posXnvl2lisa >= segPosYnvl2rival3 -72 and posXnvl2lisa <= segPosYnvl2rival3 +72):
                canvas2.delete(segImagennvl2rival3)
                segPosYnvl2rival3 = 0
                nvl2contGas2 -= 3
                

            segContXnvl2rival3 += 1
            canvas2.after(50,segMovenvl2rival3)

        #condicional al terminar la pista para recomenzar del segundo jugador
        else:
            segPosYnvl2rival3 = 0
            segContXnvl2rival3 = -300
            segActualizarnvl2rival3()
            canvas2.delete(segImagennvl2rival3)
            segImagennvl2rival3 = canvas2.create_image(segPosXnvl2rival3,segPosYnvl2rival3,image = nvl2rival3)
            segMovenvl2rival3()



    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Se hace el movimiento del jugador uno (nvl2bart)
    def movenvl2bart(event):
        global posXnvl2bart
        
        #condicional para los limites del lado izquierdo
        if (canvas2.coords(imagennvl2bart) == [130,600]):
            canvas2.move(imagennvl2bart,0,0)
            #canvas2.delete(imagennvl2bart)
            #magennvl2bartCara = canvas2.create_image(145,600,image = nvl2bartCara)
            
            
        elif (event.keysym == 'a' or event.keysym == 'A'):
            canvas2.move(imagennvl2bart,-10,0)
            posXnvl2bart-=10
            

        #condicional para los limites del lado derecho          
        if (canvas2.coords(imagennvl2bart) == [370,600]):
            canvas2.move(imagennvl2bart,0,0)
            
    
        elif (event.keysym == 'd' or event.keysym == 'D'):
            canvas2.move(imagennvl2bart,10,0)
            posXnvl2bart+=10


    """"""
    # movimiento del jugador 2 (nvl2lisa)
    def movenvl2lisa(event):
        global posXnvl2lisa

        #condicional para los limites del lado izquierdo
        if (canvas2.coords(imagennvl2lisa) == [880,600]):
            canvas2.move(imagennvl2lisa,0,0)
            
        elif (event.keysym == "Left"):
            canvas2.move(imagennvl2lisa,-10,0)
            posXnvl2lisa -= 10

        #condicional para los limites del lado derecho          
        if (canvas2.coords(imagennvl2lisa) == [1120,600]):
            canvas2.move(imagennvl2lisa,0,0)
    
        elif (event.keysym == "Right"):
            canvas2.move(imagennvl2lisa,10,0)
            posXnvl2lisa += 10

      
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Se hace el movimiento de la pista 1
    def movenvl2pista1():
        global cnvl2pista1,nvl2contnvl2puntos,nvl2contnvl2puntos2
        if (cnvl2pista1<1800):
            canvas2.move(imagennvl2pista1,0,16)
            cnvl2pista1 +=1
            canvas2.after(50,movenvl2pista1)
        elif(cnvl2pista1==1800):
            if (nvl2contnvl2puntos > nvl2contnvl2puntos2):
                ganador = Label(canvas2,text="EL GANADOR ES \n "+vr1.get(),height=8,width=20).place(x=577,y=170)
            elif (nvl2contnvl2puntos2 > nvl2contnvl2puntos):
                ganador = Label(canvas2,text="EL GANADOR ES \n "+vr2.get(),height=8,width=20).place(x=577,y=170)
            else:
                ganador = Label(canvas2,text="¡ HA HABIDO UN EMPATE !",height=5,width=20).place(x=577,y=170)
                

    #Se hace el movimiento de la pista 2
    def movenvl2pista2():
        global cnvl2pista2
        if (cnvl2pista2<1800):
            canvas2.move(imagennvl2pista2,0,16)
            cnvl2pista2 +=1
            canvas2.after(50,movenvl2pista2)
        elif(cnvl2pista2==1800):
            if (nvl2contnvl2puntos > nvl2contnvl2puntos2):
                ganador = Label(canvas2,text="EL GANADOR ES \n "+vr1.get(),height=8,width=20).place(x=577,y=170)
            elif (nvl2contnvl2puntos2 > nvl2contnvl2puntos):
                ganador = Label(canvas2,text="EL GANADOR ES \n "+vr2.get(),height=8,width=20).place(x=577,y=170)
            else:
                ganador = Label(canvas2,text="¡ HA HABIDO UN EMPATE !",height=5,width=20).place(x=577,y=170)



    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Funcion de la gasolina del jugador uno
    nvl2contGas = 100
    def nvl2gasolina1():
        global nvl2labelGas, nvl2contGas, canvas2,cnvl2pista1
        # Se crea el label donde se va a mostrar la gasolina
        nvl2labelGas = Label(ventana2)
        nvl2labelGas.config(text = "Energía : \n"+str(nvl2contGas))
        nvl2labelGas.place(x=415,y=150)
        if(nvl2contGas>0):
            nvl2contGas = nvl2contGas-1
            canvas2.after(1000,nvl2gasolina1)
        else:
            cnvl2pista1 = 1900
            
        

    # Funcion de la gasolina del jugador uno
    nvl2contGas2 = 100
    def nvl2gasolina2():
        global nvl2labelGas2, nvl2contGas2, canvas2
        # Se crea el label donde se va a mostrar la gasolina
        nvl2labelGas2 = Label(ventana2)
        nvl2labelGas2.config(text = "Energía : \n"+str(nvl2contGas2))
        nvl2labelGas2.place(x=1155,y=150)
        if(nvl2contGas2>0):
            nvl2contGas2 = nvl2contGas2 -1
            canvas2.after(1000,nvl2gasolina2)
        else:
            cnvl2pista2 = 1900
            
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    nvl2contnvl2puntos = 0
    def nvl2puntos():
        global nvl2labelnvl2puntos,nvl2contnvl2puntos,nvl2contGas
        nvl2labelnvl2puntos = Label(ventana2)
        nvl2labelnvl2puntos.config(text = "1P \n"+str(nvl2contnvl2puntos))
        nvl2labelnvl2puntos.place(x=415,y=250)
        if(nvl2contnvl2puntos>=0):
            if(nvl2contGas>0):
                nvl2contnvl2puntos += 50
            canvas2.after(1000,nvl2puntos)

    nvl2contnvl2puntos2 = 0
    def nvl2puntos2():
        global nvl2labelnvl2puntos2,nvl2contnvl2puntos2,nvl2contGas2
        nvl2labelnvl2puntos2 = Label(ventana2)
        nvl2labelnvl2puntos2.config(text = "2P \n"+str(nvl2contnvl2puntos2))
        nvl2labelnvl2puntos2.place(x=1155,y=250)
        if(nvl2contnvl2puntos2>=0):
            if(nvl2contGas2>0):
                nvl2contnvl2puntos2 += 50
            canvas2.after(1000,nvl2puntos2)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def funnvl2dona1():
        global nvl2contGas, canvas2, ventana2, nvl2dona, cnvl2dona1, imagennvl2dona, posXnvl2bart, posXnvl2dona, posYnvl2dona, posYnvl2bart,nvl2contnvl2puntos
        
        # Mueve al carro solo en y
        if(cnvl2dona1 < 220):
            canvas2.move(imagennvl2dona,0,6)
            cnvl2dona1 += 1
            posYnvl2dona +=6

            if(posXnvl2bart >= posXnvl2dona-40 and posXnvl2bart <= posXnvl2dona+40 and posYnvl2bart >= posYnvl2dona-40 and posYnvl2bart <= posYnvl2dona+40):
                if(nvl2contGas>0):
                    nvl2contGas+=7
                    nvl2contnvl2puntos += 1000
                posYnvl2dona = -200
                canvas2.delete(imagennvl2dona)
            canvas2.after(40,funnvl2dona1)

        # Cuando se termina la pista, se repite el proceso
        else:
            cnvl2dona1 = 0
            canvas2.delete(imagennvl2dona)
            posYnvl2dona = -200
            actualizarnvl2dona()
            imagennvl2dona = canvas2.create_image(posXnvl2dona,posYnvl2dona,image = nvl2dona)  
            funnvl2dona1()



    def funnvl2dona2():
        global nvl2contGas2, canvas2, ventana2, nvl2dona, cnvl2dona2, imagennvl2dona2, posXnvl2lisa, posXnvl2dona2, posYnvl2dona2, posYnvl2lisa,nvl2contnvl2puntos2
        
        # Mueve al carro solo en y
        if(cnvl2dona2 < 220):
            canvas2.move(imagennvl2dona2,0,5)
            cnvl2dona2 += 1
            posYnvl2dona2 += 5

            if(posXnvl2lisa >= posXnvl2dona2 -40 and posXnvl2lisa <= posXnvl2dona2 +40 and posYnvl2lisa >= posYnvl2dona2-40 and posYnvl2lisa <= posYnvl2dona2+40):
                if(nvl2contGas2>0):
                    nvl2contGas2 += 7
                    nvl2contnvl2puntos2 += 1000
                posYnvl2dona2 = -200
                canvas2.delete(imagennvl2dona2)
            canvas2.after(40,funnvl2dona2)
            
        # Cuando se termina la pista, se repite el proceso
        else:
            cnvl2dona2 = 0
            canvas2.delete(imagennvl2dona2)
            posYnvl2dona2 = -200
            actualizarnvl2dona2()
            imagennvl2dona2 = canvas2.create_image(posXnvl2dona2,posYnvl2dona2,image = nvl2dona)  
            funnvl2dona2()

    def nvl2iniciar(event):
        if (event.keysym == 'Tab'):
            movenvl2rival1()
            segMovenvl2rival1()
            movenvl2rival2()
            segMovenvl2rival2()
            movenvl2rival3()
            segMovenvl2rival3()
            canvas2.bind_all("<KeyPress-a>", movenvl2bart)
            canvas2.bind_all("<KeyPress-A>", movenvl2bart)
            canvas2.bind_all("<KeyPress-d>", movenvl2bart)
            canvas2.bind_all("<KeyPress-D>", movenvl2bart)
            canvas2.bind_all("<KeyPress-Left>", movenvl2lisa)
            canvas2.bind_all("<KeyPress-Right>", movenvl2lisa)
            movenvl2pista1()
            movenvl2pista2()
            nvl2gasolina1()
            nvl2gasolina2()
            funnvl2dona1()
            funnvl2dona2()
            nvl2puntos()
            nvl2puntos2()
            
    canvas2.bind_all("<KeyPress-Tab>", nvl2iniciar)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Función del nivel 3
#imagenes que saldran en el nivel 1
nvl3pista1 = PhotoImage(file="level1.PNG")
nvl3pista2 = PhotoImage(file="level1.PNG")
nvl3bart = PhotoImage(file="bart.PNG")
nvl3rival1 = PhotoImage(file="rival11.PNG")
nvl3rival2 = PhotoImage(file="rival2.PNG")
nvl3rival3 = PhotoImage(file="rival3.PNG")
nvl3lisa = PhotoImage(file="lisa.PNG")
nvl3dona = PhotoImage(file="dona.png")


#contadores que se usaran en las funciones

#nvl3rival1
cnvl3rival1 = 0
segnvl3rival1 = 0
#nvl3rival2
cnvl3rival2x = 0
segnvl3rival2x = 0
cnvl3rival2y = 0
segnvl3rival2y = 0
#pistas 1 y 2
cnvl3pista1 = 0
cnvl3pista2 = 0
#nvl3donas
cnvl3dona1 = 0
cnvl3dona2 = 0


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# seguimiento posicion nvl3bart y nvl3lisa
posXnvl3bart = 250
posYnvl3bart = 600
posXnvl3lisa = 1000
posYnvl3lisa = 600


# Actualizacion de la posicion de la nvl3dona en x
def actualizarnvl3dona():
    global posXnvl3dona
    posXnvl3dona = random.randrange(180,390)

actualizarnvl3dona()

# Actualizacion de la posicion de la nvl3dona en x del segundo jugador
def actualizarnvl3dona2():
    global posXnvl3dona2
    posXnvl3dona2 = random.randrange(890,1110)

actualizarnvl3dona2()

# Posiciones en y de nvl3donas
posYnvl3dona = -200
posYnvl3dona2 = -200


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Actualizacion de la posicion en x del rival 1
def actualizarnvl3rival1():
    global posXnvl3rival1
    posXnvl3rival1 = random.randrange(180,390)

actualizarnvl3rival1()

# Actualizacion de la posicion en x del rival 1 del segundo jugador
def segActualizarnvl3rival1():
    global segPosXnvl3rival1
    segPosXnvl3rival1 = random.randrange(890,1110)

segActualizarnvl3rival1()

# posicion en y del rival 1
posYnvl3rival1 = -400
segPosYnvl3rival1 = -400


# Actualizacion de la posicion en x del rival 1

posXnvl3rival2 = 120
segPosXnvl3rival2 = 850

posYnvl3rival2 = 0
segPosYnvl3rival2 = 0

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Actualizacion de la posicion en x del rival 3
def actualizarnvl3rival3():
    global posXnvl3rival3
    posXnvl3rival3 = random.randrange(180,390)
    
actualizarnvl3rival3()


# Actualizacion de la posicion en x del rival 3 del segundo jugador
def segActualizarnvl3rival3():
    global segPosXnvl3rival3
    segPosXnvl3rival3 = random.randrange(890,1110)
    
segActualizarnvl3rival3()

# posicion en y del rival 3
segPosYnvl3rival3 = -300
posYnvl3rival3 = -300



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Función del nivel 1
def nivel3():
    global ventana3, canvas3,imagennvl3pista1, ventanaMenu, imagennvl3rival1, imagennvl3rival2, nvl3dona, imagennvl3dona2, posXnvl3dona, posYnvl3dona
    global imagennvl3pista2, imagennvl3bart, segImagennvl3rival1, segImagennvl3rival2, nvl3contGas, nvl3contGas2, imagennvl3dona, cnvl3dona, posYnvl3bart 
    global posYnvl3lisa, posXnvl3lisa, posXnvl3dona2, posYnvl3dona2, posXnvl3bart, posYnvl3rival1,segPosYnvl3rival1,posXnvl3rival1,segPosXnvl3rival1
    global posXnvl3rival3,posYnvl3rival3,contXnvl3rival3,imagennvl3rival3,segImagennvl3rival3,segPosXnvl3rival3,segPosYnvl3rival3,segContXnvl3rival3
    global segPosXnvl3rival2,segPosYnvl3rival2,nvl3labelnvl3puntos,nvl3contnvl3puntos,nvl3labelnvl3puntos2,nvl3contnvl3puntos2,vr1,vr2
     
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #al abrir el nivel uno, se minimiza la ventana del menu
    ventanaMenu.iconify()
    ventana3 = Toplevel()
    ventana3.title("NIVEL TRES")
    
    #canvas nivel 1
    canvas3 = Canvas(ventana3, width = 1920, height = 1080, bg="black")
    canvas3.pack()
    
    #Se crean las imagenes en el canvas

    #imagenes de las pistas
    imagennvl3pista1 = canvas3.create_image(270,-14200,image = nvl3pista1)
    imagennvl3pista2 = canvas3.create_image(1012,-14200,image = nvl3pista1)

    #imagenes de los jugadores
    imagennvl3bart = canvas3.create_image(posXnvl3bart,posYnvl3bart,image = nvl3bart)
    imagennvl3lisa = canvas3.create_image(posXnvl3lisa,posYnvl3lisa,image = nvl3lisa)

    #rival 1
    imagennvl3rival1 = canvas3.create_image(posXnvl3rival1,posYnvl3rival1,image = nvl3rival1)
    segImagennvl3rival1 = canvas3.create_image(segPosXnvl3rival1,segPosYnvl3rival1,image = nvl3rival1)
    #rival 2    
    imagennvl3rival2 = canvas3.create_image(posXnvl3rival2,posYnvl3rival2,image = nvl3rival2)
    segImagennvl3rival2 = canvas3.create_image(segPosXnvl3rival2,segPosYnvl3rival2,image = nvl3rival2)
    #rival 3
    imagennvl3rival3 = canvas3.create_image(posXnvl3rival3,posYnvl3rival3,image = nvl3rival3)
    segImagennvl3rival3 = canvas3.create_image(segPosXnvl3rival3,segPosYnvl3rival3,image = nvl3rival3)

    #otras imagenes
    imagennvl3dona = canvas3.create_image(posXnvl3dona,posYnvl3dona,image = nvl3dona)
    imagennvl3dona2 = canvas3.create_image(posXnvl3dona2,posYnvl3dona2,image = nvl3dona)
    #imagennvl3bartCara = canvas3.create_image(180,600,image = nvl3bartCara)
    
    #Se coloca el nombre de los jugadores en la pantalla
    jugador1 = Label(canvas3, text = "Jugador 1 : \n" + vr1.get()).place(x=410,y=50)                
    jugador2 = Label(canvas3, text = "Jugador 2 : \n" + vr2.get()).place(x=1150,y=50)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Se crea la funcion para devolver al menu, que cierra la partida y abre el menu
    def volverMenu3():
        ventana3.destroy()
        ventanaMenu.deiconify()

    #Se hace el boton de volver al menu
    volverMenu = Button(ventana3,text="Regresar Al Menú",command=volverMenu3,bg="yellow").place(x=590,y=580)

    def siguienteNivel3():
        ventana3.destroy()
        nivel4()

    siguienteNivel = Button(ventana3,text="Siguiente Nivel",command=siguienteNivel3,bg="yellow").place(x=595,y=400)    

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # funcion del movimiento del rival 1 (carro que va en un solo carril)
    def movenvl3rival1():
        global canvas3, ventana3, nvl3rival1, cnvl3rival1, imagennvl3rival1, posYnvl3rival1,nvl3contGas,posXnvl3bart,posYnvl3bart

        # Mueve al carro solo en y
        if(cnvl3rival1 < 220):
            canvas3.move(imagennvl3rival1,0,7)
            cnvl3rival1 += 1
            posYnvl3rival1 += 7

            #se crea el choque de nvl3bart con el rival 1
            if(posXnvl3bart >= posXnvl3rival1 -37 and posXnvl3bart <= posXnvl3rival1 +37 and posYnvl3bart >= posYnvl3rival1 -76 and posYnvl3bart <= posYnvl3rival1 +76):
                nvl3contGas -= 3
                canvas3.delete(imagennvl3rival1)
                posYnvl3rival1 = -400
            canvas3.after(40,movenvl3rival1)

        # Cuando se termina la pista, se repite el proceso
        else:
            cnvl3rival1 = 0
            canvas3.delete(imagennvl3rival1)
            posYnvl3rival1 = -400
            actualizarnvl3rival1()
            imagennvl3rival1 = canvas3.create_image(posXnvl3rival1,posYnvl3rival1,image = nvl3rival1)
            movenvl3rival1()



    #funcion del rival uno para el segundo jugador
    def segMovenvl3rival1():
        global canvas3, ventana3, nvl3rival1, segnvl3rival1, segImagennvl3rival1,segPosXnvl3rival1,segPosYnvl3rival1,nvl3contGas2

        # Mueve al carro solo en y
        if(segnvl3rival1 < 220):
            canvas3.move(segImagennvl3rival1,0,7)
            segnvl3rival1 += 1
            segPosYnvl3rival1 += 7

            #se crea el choque de nvl3lisa con el rival 1
            if(posXnvl3lisa >= segPosXnvl3rival1 -37 and posXnvl3lisa <= segPosXnvl3rival1 +37 and posYnvl3lisa >= segPosYnvl3rival1 -76 and posYnvl3lisa <= segPosYnvl3rival1 +76):
                nvl3contGas2 -= 3
                canvas3.delete(segImagennvl3rival1)
                segPosYnvl3rival1 = -400
            canvas3.after(40,segMovenvl3rival1)

        # Cuando se termina la pista, se repite el proceso
        else:
            segnvl3rival1 = 0
            canvas3.delete(segImagennvl3rival1)
            segPosYnvl3rival1 = -400
            segActualizarnvl3rival1()
            segImagennvl3rival1 = canvas3.create_image(segPosXnvl3rival1,segPosYnvl3rival1,image = nvl3rival1) 
            segMovenvl3rival1()


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Movimiento del rival 2 (Carro que cambia de carril)
    def movenvl3rival2():
        global canvas3, ventana3, nvl3rival2, cnvl3rival2x, imagennvl3rival2, cnvl3rival2y,posXnvl3rival2,posYnvl3rival2, nvl3contGas

        #Se mueve diagonalmente hacia la derecha
        if (cnvl3rival2x < 53):
            canvas3.move(imagennvl3rival2,7,5)
            cnvl3rival2x += 1
            posXnvl3rival2 += 7
            posYnvl3rival2 += 5

            if(posXnvl3bart >= posXnvl3rival2 -60 and posXnvl3bart <= posXnvl3rival2 +60 and posYnvl3bart >= posYnvl3rival2 -39 and posYnvl3bart <= posYnvl3rival2 +39):
                canvas3.delete(imagennvl3rival2)
                nvl3contGas -= 3
                posYnvl3rival2 = 0
                
                
            canvas3.after(40,movenvl3rival2)    
        # Al chocar con el borde de la carretera, comienza el movimiento diagonal hacia la izquierda
        elif (cnvl3rival2x >= 53 and cnvl3rival2x < 104):
            canvas3.move(imagennvl3rival2,-7,5)
            cnvl3rival2x += 1
            cnvl3rival2y += 1
            posXnvl3rival2 -= 7
            posYnvl3rival2 += 5

            if(posXnvl3bart >= posXnvl3rival2 -60 and posXnvl3bart <= posXnvl3rival2 +60 and posYnvl3bart >= posYnvl3rival2 -39 and posYnvl3bart <= posYnvl3rival2+39):
                canvas3.delete(imagennvl3rival2)
                nvl3contGas -= 3
                posYnvl3rival2 = 0
                
            
            
            # Cuando llegue al final de la carretera, se borra la imagen y se crea de nuevo para volver a comenzar
            if(cnvl3rival2y >= random.randrange(120,200)):
                cnvl3rival2x = 0
                cnvl3rival2y = 0
                posXnvl3rival2 = 120
                posYnvl3rival2 = 0
                canvas3.delete(imagennvl3rival2)
                imagennvl3rival2 = canvas3.create_image(120,-50,image = nvl3rival2)
            canvas3.after(40,movenvl3rival2)

        # Llama de nuevo a la funcion para que se repitan los condicionales anteriores
        else:        
            cnvl3rival2x = 0
            movenvl3rival2()



    #movimiento del rival 2 para el 2do jugador
    def segMovenvl3rival2():
        global canvas3, ventana3, nvl3rival2, segnvl3rival2x, segImagennvl3rival2, segnvl3rival2y,segPosYnvl3rival2,segPosXnvl3rival2,nvl3contGas2

        #Se mueve diagonalmente hacia la derecha
        if (segnvl3rival2x < 53):
            canvas3.move(segImagennvl3rival2,7,5)
            segnvl3rival2x += 1
            segPosXnvl3rival2 += 7
            segPosYnvl3rival2 += 5

            if(posXnvl3lisa >= segPosXnvl3rival2 -60 and posXnvl3lisa <= segPosXnvl3rival2 +60 and posYnvl3lisa >= segPosYnvl3rival2 -39 and posYnvl3lisa <= segPosYnvl3rival2 +39):
                canvas3.delete(segImagennvl3rival2)
                nvl3contGas2 -= 3
                segPosYnvl3rival2 = 0
                

            canvas3.after(40,segMovenvl3rival2)   
            
        # Al chocar con el borde de la carretera, comienza el movimiento diagonal
        # hacia la izquierda
        elif (segnvl3rival2x >= 53 and segnvl3rival2x < 104):
            canvas3.move(segImagennvl3rival2,-5,3)
            segnvl3rival2x += 1
            segnvl3rival2y += 1
            segPosXnvl3rival2 -= 7
            segPosYnvl3rival2 += 5

            if(posXnvl3lisa >= segPosXnvl3rival2 -60 and posXnvl3lisa <= segPosXnvl3rival2 +60 and posYnvl3lisa >= segPosYnvl3rival2 -39 and posYnvl3lisa <= segPosYnvl3rival2 +39):
                canvas3.delete(segImagennvl3rival2)
                nvl3contGas2 -= 3
                segPosYnvl3rival2 = 0
                
            
            # Cuando llegue al final de la carretera, se borra la imagen y se crea de nuevo para volver a comenzar
            if(segnvl3rival2y >= random.randrange(120,200)):
                segnvl3rival2x = 0
                segnvl3rival2y = 0
                segPosXnvl3rival2 = 850
                segPosYnvl3rival2 = 0
                canvas3.delete(segImagennvl3rival2)
                segImagennvl3rival2 = canvas3.create_image(850,-50,image = nvl3rival2)

            canvas3.after(40,segMovenvl3rival2)   

        # Llama de nuevo a la funcion para que se repitan los condicionales anteriores
        else:        
            segnvl3rival2x = 0
            segMovenvl3rival2()


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # funcion del movimiento del rival 3 (carro que persigue al jugador)
    contXnvl3rival3 = 0
    def movenvl3rival3():
        global posYnvl3rival3,posXnvl3rival3, contXnvl3rival3,imagennvl3rival3, nvl3contGas

        # condicional mientras se mueve por la pista 
        if(contXnvl3rival3 < 180):
            
            if(posXnvl3rival3 < posXnvl3bart):
                canvas3.move(imagennvl3rival3,2.3,7)
                posXnvl3rival3 += 2.3
                posYnvl3rival3 += 7
            elif(posXnvl3rival3 > posXnvl3bart):
                canvas3.move(imagennvl3rival3,-2.3,7)
                posXnvl3rival3 -= 2.3
                posYnvl3rival3 += 7
            else:
                canvas3.move(imagennvl3rival3,0,7)
                posYnvl3rival3 += 7


            if(posXnvl3bart >= posXnvl3rival3 -45 and posXnvl3bart <= posXnvl3rival3 +45 and posYnvl3bart >= posYnvl3rival3 -72 and posYnvl3bart <= posYnvl3rival3 +72):
                canvas3.delete(imagennvl3rival3)
                nvl3contGas -= 3
                posYnvl3rival3 = 0
            

            contXnvl3rival3 += 1
            canvas3.after(50,movenvl3rival3)

        #condicional al terminar la pista para recomenzar
        else:
            posYnvl3rival3 = 0
            contXnvl3rival3 = -300
            actualizarnvl3rival3()
            canvas3.delete(imagennvl3rival3)
            imagennvl3rival3 = canvas3.create_image(posXnvl3rival3,posYnvl3rival3,image = nvl3rival3)
            movenvl3rival3()



    # funcion del movimiento del rival 3 (carro que persigue al jugador) del segundo jugador
    segContXnvl3rival3 = 0
    def segMovenvl3rival3():
        global segPosYnvl3rival3,segPosXnvl3rival3, segContXnvl3rival3,segImagennvl3rival3,nvl3contGas2

        # condicional mientras se mueve por la pista del segundo jugador
        if(segContXnvl3rival3 < 180):
            if(segPosXnvl3rival3 < posXnvl3lisa):
                canvas3.move(segImagennvl3rival3,2.3,7)
                segPosXnvl3rival3 += 2.3
                segPosYnvl3rival3 += 7
            elif(segPosXnvl3rival3 > posXnvl3lisa):
                canvas3.move(segImagennvl3rival3,-2.3,7)
                segPosXnvl3rival3 -= 2.3
                segPosYnvl3rival3 += 7
            else:
                canvas3.move(segImagennvl3rival3,0,7)
                segPosYnvl3rival3 += 7

            if(posXnvl3lisa >= segPosXnvl3rival3 -45 and posXnvl3lisa <= segPosXnvl3rival3 +45 and posXnvl3lisa >= segPosYnvl3rival3 -72 and posXnvl3lisa <= segPosYnvl3rival3 +72):
                canvas3.delete(segImagennvl3rival3)
                segPosYnvl3rival3 = 0
                nvl3contGas2 -= 3
                

            segContXnvl3rival3 += 1
            canvas3.after(50,segMovenvl3rival3)

        #condicional al terminar la pista para recomenzar del segundo jugador
        else:
            segPosYnvl3rival3 = 0
            segContXnvl3rival3 = -300
            segActualizarnvl3rival3()
            canvas3.delete(segImagennvl3rival3)
            segImagennvl3rival3 = canvas3.create_image(segPosXnvl3rival3,segPosYnvl3rival3,image = nvl3rival3)
            segMovenvl3rival3()



    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Se hace el movimiento del jugador uno (nvl3bart)
    def movenvl3bart(event):
        global posXnvl3bart
        
        #condicional para los limites del lado izquierdo
        if (canvas3.coords(imagennvl3bart) == [130,600]):
            canvas3.move(imagennvl3bart,0,0)
            
            
            
        elif (event.keysym == 'a' or event.keysym == 'A'):
            canvas3.move(imagennvl3bart,-10,0)
            posXnvl3bart-=10
            

        #condicional para los limites del lado derecho          
        if (canvas3.coords(imagennvl3bart) == [370,600]):
            canvas3.move(imagennvl3bart,0,0)
            
    
        elif (event.keysym == 'd' or event.keysym == 'D'):
            canvas3.move(imagennvl3bart,10,0)
            posXnvl3bart+=10


    """"""
    # movimiento del jugador 2 (nvl3lisa)
    def movenvl3lisa(event):
        global posXnvl3lisa

        #condicional para los limites del lado izquierdo
        if (canvas3.coords(imagennvl3lisa) == [880,600]):
            canvas3.move(imagennvl3lisa,0,0)
            
        elif (event.keysym == "Left"):
            canvas3.move(imagennvl3lisa,-10,0)
            posXnvl3lisa -= 10

        #condicional para los limites del lado derecho          
        if (canvas3.coords(imagennvl3lisa) == [1120,600]):
            canvas3.move(imagennvl3lisa,0,0)
    
        elif (event.keysym == "Right"):
            canvas3.move(imagennvl3lisa,10,0)
            posXnvl3lisa += 10

      
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #Se hace el movimiento de la pista 1
    def movenvl3pista1():
        global cnvl3pista1,nvl3contnvl3puntos,nvl3contnvl3puntos2
        if (cnvl3pista1<1800):
            canvas3.move(imagennvl3pista1,0,17)
            cnvl3pista1 +=1
            canvas3.after(50,movenvl3pista1)
        elif(cnvl3pista1==1800):
            if (nvl3contnvl3puntos > nvl3contnvl3puntos2):
                ganador = Label(canvas3,text="EL GANADOR ES \n "+vr1.get(),height=8,width=20).place(x=577,y=170)
            elif (nvl3contnvl3puntos2 > nvl3contnvl3puntos):
                ganador = Label(canvas3,text="EL GANADOR ES \n "+vr2.get(),height=8,width=20).place(x=577,y=170)
            else:
                ganador = Label(canvas3,text="¡ HA HABIDO UN EMPATE !",height=5,width=20).place(x=577,y=170)
                

    #Se hace el movimiento de la pista 2
    def movenvl3pista2():
        global cnvl3pista2
        if (cnvl3pista2<1800):
            canvas3.move(imagennvl3pista2,0,17)
            cnvl3pista2 +=1
            canvas3.after(50,movenvl3pista2)
        elif(cnvl3pista2==1800):
            if (nvl3contnvl3puntos > nvl3contnvl3puntos2):
                ganador = Label(canvas3,text="EL GANADOR ES \n "+vr1.get(),height=8,width=20).place(x=577,y=170)
            elif (nvl3contnvl3puntos2 > nvl3contnvl3puntos):
                ganador = Label(canvas3,text="EL GANADOR ES \n "+vr2.get(),height=8,width=20).place(x=577,y=170)
            else:
                ganador = Label(canvas3,text="¡ HA HABIDO UN EMPATE !",height=5,width=20).place(x=577,y=170)



    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Funcion de la gasolina del jugador uno
    nvl3contGas = 100
    def nvl3gasolina1():
        global nvl3labelGas, nvl3contGas, canvas3,cnvl3pista1
        # Se crea el label donde se va a mostrar la gasolina
        nvl3labelGas = Label(ventana3)
        nvl3labelGas.config(text = "Energía : \n"+str(nvl3contGas))
        nvl3labelGas.place(x=415,y=150)
        if(nvl3contGas>0):
            nvl3contGas = nvl3contGas-1
            canvas3.after(1000,nvl3gasolina1)
        else:
            cnvl3pista1 = 1900
            
        

    # Funcion de la gasolina del jugador uno
    nvl3contGas2 = 100
    def nvl3gasolina2():
        global nvl3labelGas2, nvl3contGas2, canvas3
        # Se crea el label donde se va a mostrar la gasolina
        nvl3labelGas2 = Label(ventana3)
        nvl3labelGas2.config(text = "Energía : \n"+str(nvl3contGas2))
        nvl3labelGas2.place(x=1155,y=150)
        if(nvl3contGas2>0):
            nvl3contGas2 = nvl3contGas2 -1
            canvas3.after(1000,nvl3gasolina2)
        else:
            cnvl3pista2 = 1900
            
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    nvl3contnvl3puntos = 0
    def nvl3puntos():
        global nvl3labelnvl3puntos,nvl3contnvl3puntos,nvl3contGas
        nvl3labelnvl3puntos = Label(ventana3)
        nvl3labelnvl3puntos.config(text = "1P \n"+str(nvl3contnvl3puntos))
        nvl3labelnvl3puntos.place(x=415,y=250)
        if(nvl3contnvl3puntos>=0):
            if(nvl3contGas>0):
                nvl3contnvl3puntos += 50
            canvas3.after(1000,nvl3puntos)

    nvl3contnvl3puntos2 = 0
    def nvl3puntos2():
        global nvl3labelnvl3puntos2,nvl3contnvl3puntos2,nvl3contGas2
        nvl3labelnvl3puntos2 = Label(ventana3)
        nvl3labelnvl3puntos2.config(text = "2P \n"+str(nvl3contnvl3puntos2))
        nvl3labelnvl3puntos2.place(x=1155,y=250)
        if(nvl3contnvl3puntos2>=0):
            if(nvl3contGas2>0):
                nvl3contnvl3puntos2 += 50
            canvas3.after(1000,nvl3puntos2)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def funnvl3dona1():
        global nvl3contGas, canvas3, ventana3, nvl3dona, cnvl3dona1, imagennvl3dona, posXnvl3bart, posXnvl3dona, posYnvl3dona, posYnvl3bart,nvl3contnvl3puntos
        
        # Mueve al carro solo en y
        if(cnvl3dona1 < 220):
            canvas3.move(imagennvl3dona,0,7)
            cnvl3dona1 += 1
            posYnvl3dona +=7

            if(posXnvl3bart >= posXnvl3dona-40 and posXnvl3bart <= posXnvl3dona+40 and posYnvl3bart >= posYnvl3dona-40 and posYnvl3bart <= posYnvl3dona+40):
                if(nvl3contGas>0):
                    nvl3contGas+=7
                    nvl3contnvl3puntos += 1000
                posYnvl3dona = -200
                canvas3.delete(imagennvl3dona)
            canvas3.after(40,funnvl3dona1)

        # Cuando se termina la pista, se repite el proceso
        else:
            cnvl3dona1 = 0
            canvas3.delete(imagennvl3dona)
            posYnvl3dona = -200
            actualizarnvl3dona()
            imagennvl3dona = canvas3.create_image(posXnvl3dona,posYnvl3dona,image = nvl3dona)  
            funnvl3dona1()



    def funnvl3dona2():
        global nvl3contGas2, canvas3, ventana3, nvl3dona, cnvl3dona2, imagennvl3dona2, posXnvl3lisa, posXnvl3dona2, posYnvl3dona2, posYnvl3lisa,nvl3contnvl3puntos2
        
        # Mueve al carro solo en y
        if(cnvl3dona2 < 220):
            canvas3.move(imagennvl3dona2,0,7)
            cnvl3dona2 += 1
            posYnvl3dona2 += 7

            if(posXnvl3lisa >= posXnvl3dona2 -40 and posXnvl3lisa <= posXnvl3dona2 +40 and posYnvl3lisa >= posYnvl3dona2-40 and posYnvl3lisa <= posYnvl3dona2+40):
                if(nvl3contGas2>0):
                    nvl3contGas2 += 7
                    nvl3contnvl3puntos2 += 1000
                posYnvl3dona2 = -200
                canvas3.delete(imagennvl3dona2)
            canvas3.after(40,funnvl3dona2)
            
        # Cuando se termina la pista, se repite el proceso
        else:
            cnvl3dona2 = 0
            canvas3.delete(imagennvl3dona2)
            posYnvl3dona2 = -200
            actualizarnvl3dona2()
            imagennvl3dona2 = canvas3.create_image(posXnvl3dona2,posYnvl3dona2,image = nvl3dona)  
            funnvl3dona2()

    def nvl3iniciar(event):
        if (event.keysym == 'Tab'):
            movenvl3rival1()
            segMovenvl3rival1()
            movenvl3rival2()
            segMovenvl3rival2()
            movenvl3rival3()
            segMovenvl3rival3()
            canvas3.bind_all("<KeyPress-a>", movenvl3bart)
            canvas3.bind_all("<KeyPress-A>", movenvl3bart)
            canvas3.bind_all("<KeyPress-d>", movenvl3bart)
            canvas3.bind_all("<KeyPress-D>", movenvl3bart)
            canvas3.bind_all("<KeyPress-Left>", movenvl3lisa)
            canvas3.bind_all("<KeyPress-Right>", movenvl3lisa)
            movenvl3pista1()
            movenvl3pista2()
            nvl3gasolina1()
            nvl3gasolina2()
            funnvl3dona1()
            funnvl3dona2()
            nvl3puntos()
            nvl3puntos2()
               
    canvas3.bind_all("<KeyPress-Tab>", nvl3iniciar)
    
#Función del nivel 4
def nivel4():
    ventanaMenu.iconify()
    ventana4 = Toplevel()
    ventana4.title("NIVEL CUATRO")
    ventana4.geometry("1920x1080")
    
#Función del nivel 5
def nivel5():
    ventanaMenu.iconify()
    ventana5 = Toplevel()
    ventana5.title("NIVEL CINCO")
    ventana5.geometry("1920x1080")

    
#imagenes del menu
menu = PhotoImage(file="portada.PNG")
opcMenu = PhotoImage(file="fondo.PNG")








""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# funcion del menu del juego
def play():
    ventana.iconify()
    global menu, opcMenu, vr1, vr2, ventanaMenu, textJug1, textJug2
    ventanaMenu = Toplevel()
    ventanaMenu.geometry("900x500")
    
    #Se coloca la imagen del menu
    fondoMenu = Label(ventanaMenu,image = menu).place(x=0,y=0)

    #se coloca un fondo para las opciones del menu
    fondoOpc = Label(ventanaMenu,image = opcMenu).place(x=310,y=40)

    #se crean las opciones del menu
    #Nombre jugador 1
    labelJug1 = Label(ventanaMenu,text = "Nombre jugador 1 : ").place(x=320,y=80)
    vr1 = StringVar()
    textJug1 = Entry(ventanaMenu,textvariable=vr1).place(x=460,y=80)

    #Nombre jugador 2
    labelJug2 = Label(ventanaMenu,text = "Nombre jugador 2 : ").place(x=320,y=120)
    vr2 = StringVar()
    textJug2 = Entry(ventanaMenu,textvariable=vr2).place(x=460,y=120)

    #Escoger el nivel
    botonN1 = Button(ventanaMenu,text="NIVEL 1",command=nivel1,bg="yellow").place(x=380,y=180)
    botonN2 = Button(ventanaMenu,text="NIVEL 2",command=nivel2,bg="yellow").place(x=480,y=180)
    botonN3 = Button(ventanaMenu,text="NIVEL 3",command=nivel3,bg="yellow").place(x=330,y=210)
    botonN4 = Button(ventanaMenu,text="NIVEL 4",command=nivel4,bg="yellow").place(x=430,y=210)
    botonN5 = Button(ventanaMenu,text="NIVEL 5",command=nivel5,bg="yellow").place(x=530,y=210)

#Botones al inicio del juego
botonPlay = Button(ventana,height=3,width=10,text="PLAY",command=play,bg="pink").place(x=100,y=400)
botonInstruc = Button(ventana,height=3,width=20,text="INSTRUCCIONES",command=instrucciones,bg="pink").place(x=350,y=400)
botonAband = Button(ventana,height=3,width=20,text="ABANDONAR",command=ventana.destroy,bg="pink").place(x=710,y=400)

