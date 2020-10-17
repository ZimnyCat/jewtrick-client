from time import sleep
from mcstatus import MinecraftServer
import requests
import pyautogui

requests_counter = 0
clicked = 0

print("─╔╦═╦╦═╦╗╔══╦═╦══╦═╦╦╗")
print("─║║╦╣║║║║╚╗╔╣╬╠║║╣╔╣╔╝")
print("╔╣║╩╣║║║║─║║║╗╬║║╣╚╣╚╗")
print("╚═╩═╩═╩═╝─╚╝╚╩╩══╩═╩╩╝")
print("jew trick (client) v2.0-beta\nhttps://jewtrick.ml")
print("")
motd = requests.get("https://jewtrick.ml/server/motdv13.html")
if motd.status_code == 200:
    print(motd.text)
print("")
print("Включить AutoClick?")
print("Эта функция сделает двойной клик мышкой, когда придёт время заходить на 2b2t.\nВы можете просто навести курсор мыши на 2b2t в списке серверов и ждать.\nНапишите 'да' или 'нет'")
while True:
    response = input()
    if response != "да" and response != "нет":
        print("Напишите 'да' или 'нет'")
    else:
        break
while True:
    request_delay = 1
    requests_counter = requests_counter + 1
    try:
        jew_int = int(requests.get("https://jewtrick.ml/server/jewtrickstatus.html").text)
        if jew_int == 2:
            request_delay = 2
            jew_online = requests.get("https://jewtrick.ml/server/jew_online.html").text
            try:
                online = MinecraftServer.lookup("2b2t.org").status().players.online
                print("JEW TRICK TIME!!! Онлайн 2b2t (сервер jew trick):", jew_online, "Онлайн 2b2t (запрос):", online, "(" + str(requests_counter) + ")")
                if response == "да" and clicked == 0:
                    pyautogui.doubleClick(button="left")
                clicked = 1
            except:
                print("jew trick сейчас невозможен (" + str(requests_counter) + ")")
        elif jew_int == 1:
            print("jew trick сейчас невозможен (" + str(requests_counter) + ")")
            clicked = 0
        elif jew_int == 0:
            print("2b2t не отвечает (" + str(requests_counter) + ")")
    except:
        if requests.get("https://jewtrick.ml/server/jewtrickstatus.html").status_code == 200:
            print("Сервер jew trick получает онлайн 2b2t (" + str(requests_counter) + ")")
        else:
            print("Сервер jew trick недоступен (" + str(requests_counter) + ")")
    sleep(request_delay)