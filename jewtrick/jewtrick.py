print("Загрузка...\n")

ver = "2.3-beta"

from time import sleep
from mcstatus import MinecraftServer
import requests
import utils.settings as s
import utils.system as sys

requests_counter = 0
clicked = False

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
    try:
        request_delay = s.getNum("delay")
        jt_status = int(requests.get("http://server.jewtrick.xyz/jewtrickstatus.html").text)
        if jt_status == 2:
            request_delay += 1
            jew_online = requests.get("http://server.jewtrick.xyz/jew_online.html").text
            if not s.getBoolean("ping"):
                sys.sendMsg("JEW TRICK TIME!!! Онлайн 2b2t: " + jew_online, requests_counter)
                clicked = sys.click(clicked)
            else:
                try:
                    online = MinecraftServer.lookup("2b2t.org").status().players.online
                    sys.sendMsg("JEW TRICK TIME!!! Онлайн 2b2t (сервер jew trick): " + jew_online +
                                " Онлайн 2b2t (запрос): " + online, requests_counter)
                    clicked = sys.click(clicked)
                except:
                    sys.sendMsg("Вход без очереди сейчас невозможен", requests_counter)
        elif jt_status == 1:
            sys.sendMsg("Вход без очереди сейчас невозможен", requests_counter)
            clicked = False
        elif jt_status == 0:
            sys.sendMsg("2b2t не отвечает", requests_counter)
    except ConnectionError:
        sys.sendMsg("Сервер jew trick недоступен", requests_counter)
    except:
        sys.sendMsg("Сервер jew trick получает онлайн 2b2t", requests_counter)
    sleep(request_delay)
