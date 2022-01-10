import time
import RPi.GPIO as pino
import serial

pino.setmode(pino.BOARD)

SENSOR = 37
MOTORA1 = 3
MOTORA2 = 5
PWM_SAIDA = 7

pino.setup(SENSOR,pino.IN)

pino.setup(MOTORA1,pino.OUT)

pino.setup(MOTORA2,pino.OUT)

pino.setup(PWM_SAIDA,pino.OUT)

p = pino.PWM(PWM_SAIDA,100)


pino.output(MOTORA1,True)
pino.output(MOTORA2,False)
p.start(0)

sentido = True
ll = '0'

print('Start')
port= '/dev/rfcomm0'
bluetooth = serial.Serial(port,9600,timeout=0.050)
print('Conected')
bluetooth.flushInput()

def mede_velocidade():
    print("Medindo a velocidade ...")
    tempo = time.time()
    cont = 0
    antigo = 0
    while (time.time() - tempo ) < 10:
        if pino.input(SENSOR) != antigo:
            cont = cont+1
            antigo = pino.input(SENSOR)
            print("tempo que falta",10 - round(time.time() - tempo))
    velocidade = cont / 20
    print("Velocidade medida -->",velocidade)
    return velocidade       
    
    return velocidade
def seta_velocidade(pwm,dire):
    if dire:
        pino.output(MOTORA1,True)
        pino.output(MOTORA2,False)
    else:
        pino.output(MOTORA1,False)
        pino.output(MOTORA2,True)
    
    #print("Set velocidade")
    p.ChangeDutyCycle(pwm)
    pino.output(PWM_SAIDA,True)
def envia_velocidade(velocidade):
    print("Enviando a velocidade --> ",velocidade)
    #for i in range(1):
    bluetooth.write(str(velocidade).encode())
    time.sleep(1)
    bluetooth.flushInput()    

def controle():
    global ll
    global velocidade_antiga
    global sentido
    #bluetooth.flushInput()
    while True:
        if bluetooth.in_waiting>0:

            l = bluetooth.read(size=8)
            ll = l.decode()
            #print(ll)
            if ll == '10':
                if velocidade_antiga == 100: continue
                print("aumentei")
                velocidade  = velocidade_antiga + 10
                seta_velocidade(pwm = velocidade,dire = sentido)
                velocidade_antiga = velocidade
            if ll == '11':
                if velocidade_antiga == 0: continue

                velocidade  = velocidade_antiga - 10
                seta_velocidade(pwm= velocidade,dire = sentido)
                velocidade_antiga = velocidade
            if ll == '20' : 
                sentido = True
                seta_velocidade(pwm= velocidade,dire = sentido)
            if ll == '21' : 
                sentido = False
                seta_velocidade(pwm= velocidade,dire = sentido)

        print("velocidade",velocidade_antiga)

if __name__ == '__main__':
    lido = 55
    ler = 33
    while True:
        
        if bluetooth.in_waiting>0:
            lido = bluetooth.read(size=8)
            ler = lido.decode()
            print(ler)
        if ler == '0': 
            velocidade_antiga = 20
            seta_velocidade(pwm = velocidade_antiga,dire = sentido)
            controle()

        if ler == '1' : 
            seta_velocidade(pwm = 100,dire = sentido)

            velocidade = mede_velocidade()

            envia_velocidade(velocidade)
            






    
