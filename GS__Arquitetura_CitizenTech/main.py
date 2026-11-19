"""CitizenTech - Alerta Inteligente de Enchentes.

Global Solution 2026.2 | Raspberry Pi Pico + MicroPython + Wokwi.
O HC-SR04 representa um sensor fixo 100 cm acima da base de referencia.
O prototipo e didatico e NAO e um sistema de seguranca para uso real.
"""
from machine import Pin, PWM, time_pulse_us
from time import sleep_us, sleep_ms

# Portas do Raspberry Pi Pico
TRIG = Pin(2, Pin.OUT)
ECHO = Pin(3, Pin.IN)
LED_VERDE = Pin(13, Pin.OUT)
LED_AMARELO = Pin(14, Pin.OUT)
LED_VERMELHO = Pin(15, Pin.OUT)
BUZZER = PWM(Pin(16))
BUZZER.freq(1000)
BUZZER.duty_u16(0)

# Premissas ilustrativas (nao sao limites oficiais de enchente)
ALTURA_REFERENCIA_CM = 100.0
LIMIAR_ATENCAO = 40.0
LIMIAR_PERIGO = 75.0


def medir_distancia_cm():
    """Dispara o sensor e devolve distancia em cm, ou None se houver falha."""
    TRIG.value(0)
    sleep_us(2)
    TRIG.value(1)
    sleep_us(10)
    TRIG.value(0)

    duracao_us = time_pulse_us(ECHO, 1, 30000)
    if duracao_us < 0:
        return None
    return duracao_us / 58.0


def nivel_percentual(distancia_cm):
    """Estima o percentual de agua no intervalo de referencia (0 a 100 cm)."""
    altura_cm = ALTURA_REFERENCIA_CM - distancia_cm
    altura_cm = max(0.0, min(ALTURA_REFERENCIA_CM, altura_cm))
    return 100.0 * altura_cm / ALTURA_REFERENCIA_CM


def classificar_nivel(percentual):
    if percentual >= LIMIAR_PERIGO:
        return "PERIGO"
    if percentual >= LIMIAR_ATENCAO:
        return "ATENCAO"
    return "NORMAL"


def atualizar_leds(estado):
    LED_VERDE.value(estado == "NORMAL")
    LED_AMARELO.value(estado == "ATENCAO")
    LED_VERMELHO.value(estado == "PERIGO")


def alerta_sonoro(estado):
    if estado == "PERIGO":
        BUZZER.duty_u16(18000)
        sleep_ms(220)
        BUZZER.duty_u16(0)
        sleep_ms(500)
    else:
        BUZZER.duty_u16(0)
        sleep_ms(720)


print("============================================")
print("CITIZENTECH - ALERTA INTELIGENTE DE ENCHENTES")
print("Sensor HC-SR04 + LEDs + buzzer | Pico")
print("Distancia menor = nivel da agua maior")
print("============================================")

while True:
    distancia = medir_distancia_cm()
    if distancia is None:
        # Falha de leitura: sinalizamos falha e evitamos declarar seguranca.
        LED_VERDE.off()
        LED_AMARELO.on()
        LED_VERMELHO.off()
        BUZZER.duty_u16(0)
        print("Falha na leitura do sensor. Verifique conexoes.")
        sleep_ms(720)
        continue

    percentual = nivel_percentual(distancia)
    estado = classificar_nivel(percentual)
    atualizar_leds(estado)
    print("Distancia: {:.1f} cm | Nivel: {:.1f}% | Status: {}".format(
        distancia, percentual, estado
    ))
    alerta_sonoro(estado)
