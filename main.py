from machine import Pin, PWM, ADC
from time import sleep
import math
import time


def przesuniecie(stopien, serwo):
    czas_podstawowy = 0.011
    czas = 0.011 * (stopien/2)
    serwo.duty_ns(1434890)
    sleep(czas)
    serwo.duty_ns(1500000)
    
def cofniecie(stopien, serwo):
    czas_podstawowy = 0.011
    czas = 0.011 * (stopien/2)
    serwo.duty_ns(1500000-1434890+1500000)
    sleep(czas)
    serwo.duty_ns(1500000)

serwoD = PWM(machine.Pin(15))
serwoG = PWM(machine.Pin(14))
serwoD.freq(50)
serwoG.freq(50)

fotorezystor2 = machine.ADC(26)
fotorezystor1 = machine.ADC(27)

wartosc_poprzednia = 0
wartosc_obecna = 0

kierunek = 1 # true - w gore. false - w dol

stopnie = 90 #ustawienie poczatkowe kata slonca
while True: #glowna petla
    wartosc1 = fotorezystor1.read_u16()
    wartosc2 = fotorezystor2.read_u16()
    roznica = math.fabs(wartosc1-wartosc2)
    #print(roznica)
    if roznica > 1000:
        if wartosc1 > wartosc2:
            przesuniecie(5, serwoD)
            time.sleep(0.5)
        if wartosc1 < wartosc2:
            cofniecie(5, serwoD)
            time.sleep(0.5)
    else:
        wartosc_poprzednia = wartosc_obecna
        wartosc_obecna = fotorezystor1.read_u16()
        if math.fabs(wartosc_poprzednia-wartosc_obecna) > 80:
            if wartosc_poprzednia < wartosc_obecna:
                if kierunek ==0:
                    kierunek = 1
                else:
                    kierunek = 0
            if kierunek == 0:
                cofniecie(5, serwoG)
                stopnie-=5
            else:
                przesuniecie(5, serwoG)
                stopnie+=5
        time.sleep(0.5)
    time.sleep(1)
