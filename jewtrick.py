print("Загрузка...\n")

ver = "2.2"

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
print("jew trick (client) " + ver + "\nhttps://jewtrick.xyz/\n")
lastver = requests.get("http://server.jewtrick.xyz/lastversion.html").text
if lastver == ver:
    motd = requests.get("http://server.jewtrick.xyz/motdv22.html")
    if motd.status_code == 200:
        print(motd.text + "\n")
else:
    print("Обновитесь до новейшей версии jew trick " + lastver + " на https://jewtrick.xyz/")
for word in s.booleanArray:
    print(word, "=", s.getBoolean(word))
for word in s.numArray:
    print(word, "=", s.getNum(word))
print("")
while True:
    global request_delay
    requests_counter += 1
    time = _time()
    try:
        request_delay = s.getNum("delay")
        jt_status = int(requests.get("http://server.jewtrick.xyz/jewtrickstatus.html").text)

        if jt_status == 2:
            request_delay += 1
            jew_online = requests.get("http://server.jewtrick.xyz/jew_online.html").text
            if not s.getBoolean("ping"):
                print(time + "JEW TRICK TIME!!! Онлайн 2b2t:", jew_online)
                clicked = _click(clicked)
            else:
                try:
                    online = MinecraftServer.lookup("2b2t.org").status().players.online
                    print(time + "JEW TRICK TIME!!! Онлайн 2b2t (сервер jew trick):", jew_online,
                          "Онлайн 2b2t (запрос):",
                          online, "(" + str(requests_counter) + ")")
                    clicked = _click(clicked)
                except:
                    print(time + "Вход без очереди сейчас невозможен (" + str(requests_counter) + ")")
        elif jt_status == 1:
            print(time + "Вход без очереди сейчас невозможен (" + str(requests_counter) + ")")
            clicked = False
        elif jt_status == 0:
            print(time + "2b2t не отвечает (" + str(requests_counter) + ")")
    except ConnectionError:
        print(time + "Сервер jew trick недоступен (" + str(requests_counter) + ")")
    except:
        print(time + "Сервер jew trick получает онлайн 2b2t (" + str(requests_counter) + ")")
    sleep(request_delay)
