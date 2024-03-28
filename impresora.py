from conexion import *
import os

def imprimir(ruta_imagen):
    with Image.open(ruta_imagen).convert("1") as im:
        pix = im.load()
        y = 0
        while y != 120:
            if y % 2 != 0:
                for x in reversed(range(320)):
                    if pix[x, y] < 125:
                        cerrar_rele_3()
                        print("Draw")
                    cerrar_rele_1()
                    print("Left")
            elif y % 2 == 0:
                for x in (range(320)):
                    if pix[x,y] < 125:
                        cerrar_rele_3()
                        print("Draw")
                    cerrar_rele_0()
                    print("Right")
            y += 1
            print("Down")
            cerrar_rele_2()
        return

#-------------------------------------------------------------------------

def imprimir_optimizado(ruta_imagen):
    with Image.open(ruta_imagen).convert("1") as im:
        imagen = im.load()
        posX = 0
        posY = 0
        while posY != 120:

#-----------------------------------------------------------------------------
#                      Fase de analisis:
            
            analisis = analizar_linea(imagen, posY)
            if len(analisis) == 0:
                #Skip line if empty
                cerrar_rele_2()
                posY = posY +1
                print("Down")

#-----------------------------------------------------------------------------
#                      MOVE PHASE:
                
            else:
                #Move to closest pixel
                objetivo = closest_pixel(posX, analisis[0], analisis[1])
                #Moving towards left
                if posX > objetivo:
                    while posX != objetivo:
                        cerrar_rele_1()
                        posX = posX -1
                        print("Left")
                #Moving towards right      
                elif posX < objetivo:
                    while posX != objetivo:
                        cerrar_rele_0()
                        posX = posX +1
                        print("Right")

#-----------------------------------------------------------------------------
#                     DRAW PHASE:

                #Drawing towards right
                if posX == analisis[0]:
                    while posX != analisis[1]:
                        if imagen[posX, posY] < 125:
                            cerrar_rele_3()
                            print("Draw")
                        cerrar_rele_0()
                        posX = posX +1
                        print("Right")
                
                #Drawing towards left
                elif posX == analisis[1]:
                    while posX != analisis[0]:
                        if imagen[posX, posY] < 125:
                            cerrar_rele_3()
                            print("Draw")
                        cerrar_rele_1()
                        posX = posX -1
                        print("Left")

#-----------------------------------------------------------------------------
#                   END OF LINE:

                #End of line
                cerrar_rele_2()
                posY = posY +1
                print("Down")
                

                






def analizar_linea(imagen, Y):
    '''
    Returns x,y of first and last black pixel on the line given
    '''
    res = []
    for x in (range(320)):
        if imagen[x, Y] < 125:
            res.append(x)
    if len(res) == 0:
        return ()
    return (res[0],res[-1])
        
def closest_pixel(posX, pix_izquierdo, pix_derecho):
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
    print("REMEMBER: Ctrl + c to stop execution")
    res = input("PROGRAM READY [1 -> Version 1.0 // 2 -> Version 2.0, any other key to cancel]:")
    nombre_archivo = input("File name (File sufix must be included, for example: 'Demo.png')")
    ruta_imagen = os.path.join("Imagenes", nombre_archivo)
    if res == "1":
        cerrar_rele_3()
        time.sleep(2)
        cerrar_rele_3()
        time.sleep(1)
        imprimir(ruta_imagen)
    if res == "2":
        cerrar_rele_3()
        time.sleep(2)
        cerrar_rele_3()
        time.sleep(1)
        imprimir_optimizado(ruta_imagen)
    return

if __name__ == "__main__": 
    ejecutar()
    #test_infinito()