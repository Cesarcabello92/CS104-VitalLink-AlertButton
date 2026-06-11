import time
import RPi.GPIO as GPIO
import requests

BOT_TOKEN = "8953845136:AAHSmyiXfn4lUpl45fHmN19QEWhK_AmkC3E"
CHAT_ID = "1476379787"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=data)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        send_telegram("Someone pressed the alert button!")
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)


