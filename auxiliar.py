from conexion import *

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




def estimated_time(line, ruta_imagen, posX = 0):
    ETA = 0
    with Image.open(ruta_imagen).convert("1") as im:
        imagen = im.load()
        posY = line
        while posY != 120:
            
            analisis = analizar_linea(imagen, posY)
            if len(analisis) == 0:
                #Skip line if empty
                ETA = ETA + cierre + tiempo
                posY = posY +1

#-----------------------------------------------------------------------------
#                      MOVE PHASE:
                
            else:
                #Move to closest pixel
                objetivo = closest_pixel(posX, analisis[0], analisis[1])
                #Moving towards left
                if posX > objetivo:
                    while posX != objetivo:
                        ETA = ETA +  cierre + tiempo
                        posX = posX -1
                #Moving towards right      
                elif posX < objetivo:
                    while posX != objetivo:
                        ETA = ETA +  cierre + tiempo
                        posX = posX +1

#-----------------------------------------------------------------------------
#                     DRAW PHASE:

                #Drawing towards right
                if posX == analisis[0]:
                    while posX != analisis[1]:
                        if imagen[posX, posY] < 125:
                            ETA = ETA +  cierre + tiempo
                        ETA = ETA +  cierre + tiempo
                        posX = posX +1
                
                #Drawing towards left
                elif posX == analisis[1]:
                    while posX != analisis[0]:
                        if imagen[posX, posY] < 125:
                            ETA = ETA +  cierre + tiempo
                        ETA = ETA +  cierre + tiempo
                        posX = posX -1

#-----------------------------------------------------------------------------
#                   END OF LINE:

                #End of line
                ETA = ETA +  cierre + tiempo
                posY = posY +1
    return convert_seconds(ETA)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    formatted_time = ""
    if hours > 0:
        formatted_time += f"{int(hours)} hour(s) "
    if minutes > 0:
        formatted_time += f"{int(minutes)} minute(s) "
    if seconds > 0:
        formatted_time += f"{int(seconds)} second(s)"

    return formatted_time.strip()