import cv2
import numpy as np
import time
import Adafruit_BBIO.PWM as PWM

CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4
LARGURA_FOTO = 320
ALTURA_FOTO = 240
T_FOTO = 150
L_FOTO = 130
LIBERAR = 4
FECHAR = 3
POSICAO_AZUL = 0
POSICAO_VERDE = 90
POSICAO_VERMELHO = 180

servoPinObjetos="P9_21"
servoPinCopos="P9_14"

def tirarFoto():
    capture = cv2.VideoCapture(0)

    capture.set(CV_CAP_PROP_FRAME_WIDTH, LARGURA_FOTO)
    capture.set(CV_CAP_PROP_FRAME_HEIGHT, ALTURA_FOTO)

    ret, frame = capture.read()

    cv2.imwrite('foto.jpg', frame)

    capture.release()
    cv2.destroyAllWindows()
    
def analisarPixels(T, L):
    img = cv2.imread('foto.jpg')
    
    b = img[T, L, 0]
    g = img[T, L, 1]
    r = img[T, L, 2]
    
    if b > g and b > r:
        return 1
    elif g > b and g > r:
        return 2
    elif r > b and r > g:
        return 3
        
    return 0

def Motor_Liberar_Objeto(ciclo):
    PWM.set_duty_cycle(servoPinObjetos, ciclo)
		
def Motor_Copos(angulo):
    ciclo=1./18.*angulo + 5
    PWM.set_duty_cycle(servoPinCopos, ciclo)
		
def main():
    PWM.start(servoPinObjetos, 3, 50)
    PWM.start(servoPinCopos, 5, 50)
    
    tirarFoto()
    
    #(T, L)
    cor = analisarPixels(T_FOTO, L_FOTO)

    #BGR
    if cor == 1:
        print "Eh azul!"
        
        Motor_Copos(POSICAO_AZUL)
        
        time.sleep(3)
        
        Motor_Liberar_Objeto(LIBERAR)
        
        time.sleep(3)
        
        Motor_Liberar_Objeto(FECHAR)
    elif cor == 2:
        print "Eh verde!"
        
        Motor_Copos(POSICAO_VERDE)
        
        time.sleep(3)
        
        Motor_Liberar_Objeto(LIBERAR)
        
        time.sleep(3)
        
        Motor_Liberar_Objeto(FECHAR)
    elif cor == 3:
        print "Eh vermelho!"
        
        Motor_Copos(POSICAO_VERMELHO)
        
        time.sleep(3)
        
        Motor_Liberar_Objeto(LIBERAR)
        
        time.sleep(3)
        
        Motor_Liberar_Objeto(FECHAR)

if __name__ == '__main__':
    main()