from time import sleep
from mcstatus import MinecraftServer
import requests
import pyautogui
import settings.setting as s
from datetime import datetime

requests_counter = 0
clicked = False


def _click(val):
    if s.getBoolean("autoclick") and not val:
        pyautogui.doubleClick(button="left")
        return True
    return val


def _time():
    if s.getBoolean("time"):
        return str("[" + datetime.today().strftime("%H:%M:%S") + "] ")
    else:
        return ""


print("─╔╦═╦╦═╦╗╔══╦═╦══╦═╦╦╗")
print("─║║╦╣║║║║╚╗╔╣╬╠║║╣╔╣╔╝")
print("╔╣║╩╣║║║║─║║║╗╬║║╣╚╣╚╗")
print("╚═╩═╩═╩═╝─╚╝╚╩╩══╩═╩╩╝")
print("jew trick (client) v2.2-beta\nhttps://jewtrick.ml\n\n")
print("")
motd = requests.get("https://jewtrick.ml/server/motdv21.html")
if motd.status_code == 200:
    print(motd.text + "\n")
for word in s.booleanArray:
    print(word, "=", s.getBoolean(word))
print("")
while True:
    global request_delay
    requests_counter += 1
    try:
        request_delay = 1
        time = _time()
        jt_status = int(requests.get("https://jewtrick.ml/server/jewtrickstatus.html").text)

        if jt_status == 2:
            if s.getBoolean("request-delay"):
                request_delay = 2
            jew_online = requests.get("https://jewtrick.ml/server/jew_online.html").text
            if not s.getBoolean("ping"):
                print(time + "JEW TRICK TIME!!! Онлайн 2b2t:", jew_online)
                clicked = _click(clicked)
            else:
                try:
                    online = MinecraftServer.lookup("2b2t.org").status().players.online
                    print(time + "JEW TRICK TIME!!! Онлайн 2b2t (сервер jew trick):", jew_online, "Онлайн 2b2t (запрос):",
                          online, "(" + str(requests_counter) + ")")
                    clicked = _click(clicked)
                except:
                    print(time + "jew trick сейчас невозможен (" + str(requests_counter) + ")")
        elif jt_status == 1:
            print(time + "jew trick сейчас невозможен (" + str(requests_counter) + ")")
            clicked = False
        elif jt_status == 0:
            print(time + "2b2t не отвечает (" + str(requests_counter) + ")")
    except:
        if requests.get("https://jewtrick.ml/server/jewtrickstatus.html").status_code == 200:
            print(time + "Сервер jew trick получает онлайн 2b2t (" + str(requests_counter) + ")")
        else:
            print(time + "Сервер jew trick недоступен (" + str(requests_counter) + ")")
    sleep(request_delay)
