# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

led = [37, 35, 33, 31, 29, 27]  # LED'ler için bir liste

GPIO.setmode(GPIO.BOARD)  # Fiziksel pin numaralandırılması
GPIO.setwarnings(False)  # Uyarıları kapat

GPIO.setup(led, GPIO.OUT)  # Bütün pinleri çıkış yap

"""
Listelerde sayım sıfırdan başlar.
"""

while True:  # Sonsuz döngü
    """ SOLDAN SAĞA """
    ###########################################
    GPIO.output(led[0], GPIO.HIGH)  # 1. LED yandı
    sleep(0.1)
    GPIO.output(led[0], GPIO.LOW)  # 1. LED söndü
    GPIO.output(led[1], GPIO.HIGH)  # 2. LED yandı
    sleep(0.1)
    GPIO.output(led[1], GPIO.LOW)  # 2. LED söndü
    GPIO.output(led[2], GPIO.HIGH)  # 3. LED yandı
    sleep(0.1)
    GPIO.output(led[2], GPIO.LOW)  # 3. LED söndü
    GPIO.output(led[3], GPIO.HIGH)  # 4. LED yandı
    sleep(0.1)
    GPIO.output(led[3], GPIO.LOW)  # 4. LED söndü
    GPIO.output(led[4], GPIO.HIGH)  # 5. LED yandı
    sleep(0.1)
    GPIO.output(led[4], GPIO.LOW)  # 5. LED söndü
    GPIO.output(led[5], GPIO.HIGH)  # 6. LED yandı
    sleep(0.1)
    GPIO.output(led[5], GPIO.LOW)  # 6. LED söndü

    """ SAĞDAN SOLA """
    ###########################################
    GPIO.output(led[4], GPIO.HIGH)  # 5. LED yandı
    sleep(0.1)
    GPIO.output(led[4], GPIO.LOW)  # 5. LED söndü
    GPIO.output(led[3], GPIO.HIGH)  # 4. LED yandı
    sleep(0.1)
    GPIO.output(led[3], GPIO.LOW)  # 4. LED söndü
    GPIO.output(led[2], GPIO.HIGH)  # 3. LED yandı
    sleep(0.1)
    GPIO.output(led[2], GPIO.LOW)  # 3. LED söndü
    GPIO.output(led[1], GPIO.HIGH)  # 2. LED yandı
    sleep(0.1)
    GPIO.output(led[1], GPIO.LOW)  # 2. LED söndü
