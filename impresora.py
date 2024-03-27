from conexion import *
import os

ruta_imagen = os.path.join("Imagenes", "demo7.png")

def imprimir():
    with Image.open(ruta_imagen).convert("1") as im:
        pix = im.load()
        y = 0
        while y != 120:
            if y % 2 != 0:
                for x in reversed(range(320)):
                    if pix[x, y] < 125:
                        cerrar_rele_3()
                        print("Dibuja")
                    cerrar_rele_1()
                    print("Izquierda")
            elif y % 2 == 0:
                for x in (range(320)):
                    if pix[x,y] < 125:
                        cerrar_rele_3()
                        print("Dibuja")
                    cerrar_rele_0()
                    print("Derecha")
            y += 1
            print("Abajo")
            cerrar_rele_2()
        return

#-------------------------------------------------------------------------

def imprimir_optimizado():
    with Image.open(ruta_imagen).convert("1") as im:
        imagen = im.load()
        posX = 0
        posY = 0
        while posY != 120:

#-----------------------------------------------------------------------------
#                      Fase de analisis:
            
            analisis = analizar_linea(imagen, posY)
            if len(analisis) == 0:
                #Bajar linea si está vacia
                cerrar_rele_2()
                posY = posY +1
                print("Abajo")

#-----------------------------------------------------------------------------
#                      Fase de movimiento:
                
            else:
                #Nos movemos al pixel más cercano
                objetivo = pixel_mas_cercano(posX, analisis[0], analisis[1])
                #En caso de que haya que moverse a la izquierda
                if posX > objetivo:
                    while posX != objetivo:
                        cerrar_rele_1()
                        posX = posX -1
                        print("Izquierda")
                #En caso de que haya que moverse a la derecha        
                elif posX < objetivo:
                    while posX != objetivo:
                        cerrar_rele_0()
                        posX = posX +1
                        print("Derecha")

#-----------------------------------------------------------------------------
#                      Fase de dibujo:

                #Tenemos que dibujar hacia la derecha
                if posX == analisis[0]:
                    while posX != analisis[1]:
                        if imagen[posX, posY] < 125:
                            cerrar_rele_3()
                            print("Dibuja")
                        cerrar_rele_0()
                        posX = posX +1
                        print("Derecha")
                
                #Tenemos que dibujar hacia la izquierda
                elif posX == analisis[1]:
                    while posX != analisis[0]:
                        if imagen[posX, posY] < 125:
                            cerrar_rele_3()
                            print("Dibuja")
                        cerrar_rele_1()
                        posX = posX -1
                        print("Izquierda")

#-----------------------------------------------------------------------------
#                   Fase de fin de linea:

                #Fin de linea
                cerrar_rele_2()
                posY = posY +1
                print("Abajo")
                

                






def analizar_linea(imagen, Y):
    '''
    Devuelve las coordenadas del primer y ultimo pixel que hay que pintar en la linea dada
    '''
    res = []
    for x in (range(320)):
        if imagen[x, Y] < 125:
            res.append(x)
    if len(res) == 0:
        return ()
    return (res[0],res[-1])
        
def pixel_mas_cercano(posX, pix_izquierdo, pix_derecho):
  diferencia_1 = abs(posX - pix_izquierdo)
  diferencia_2 = abs(posX - pix_derecho)

  if diferencia_1 < diferencia_2:
    return pix_izquierdo
  elif diferencia_1 > diferencia_2:
    return pix_derecho
  else:
    return pix_izquierdo


def ejecutar():
    inicio()
    print("RECUERDA: Ctrl + c Para parar un programa manualmente")
    res = input("PROGRAMA LISTO [1 -> Versión 1.0 // 2 -> Versión 2.0, cualquier otra cosa para cancelar]:")
    if res == "1":
        cerrar_rele_3()
        time.sleep(2)
        cerrar_rele_3()
        time.sleep(1)
        imprimir()
    if res == "2":
        cerrar_rele_3()
        time.sleep(2)
        cerrar_rele_3()
        time.sleep(1)
        imprimir_optimizado()
    return

if __name__ == "__main__": 
    ejecutar()
    #test_infinito()
    '''with Image.open(ruta_imagen).convert("1") as im:
        pix = im.load()
        print(pix[10,10])'''