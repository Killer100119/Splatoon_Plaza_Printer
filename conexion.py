import serial
import time
from PIL import Image
tiempo = 0.075
cierre = 0.035

ser = serial.Serial('COM3', 9600)

def cerrar_rele_0():
    ser.write(b'0')
    ser.write(b'0')
    time.sleep(cierre)
    ser.write(b'0')
    ser.write(b'1')
    time.sleep(tiempo)

def cerrar_rele_1():
    ser.write(b'1')
    ser.write(b'0')
    time.sleep(cierre)
    ser.write(b'1')
    ser.write(b'1')
    time.sleep(tiempo)

def cerrar_rele_2():
    ser.write(b'2')
    ser.write(b'0')
    time.sleep(cierre)
    ser.write(b'2')
    ser.write(b'1')
    time.sleep(tiempo)

def cerrar_rele_3():
    ser.write(b'3')
    ser.write(b'0')
    time.sleep(cierre)
    ser.write(b'3')
    ser.write(b'1')
    time.sleep(tiempo)

def inicio():
    time.sleep(2.5)
    cerrar_rele_0()
    cerrar_rele_1()
    cerrar_rele_2()
    cerrar_rele_3()

def test_infinito():
    while True:
        cerrar_rele_0()
        cerrar_rele_1()
        cerrar_rele_2()
        cerrar_rele_3()
    return

'''
Relé 0: Derecha
Relé 1: Izquierda
Relé 2: Abajo
Relé 3: Dibujar
'''

