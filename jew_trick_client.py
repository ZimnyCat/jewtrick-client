from time import sleep
from mcstatus import MinecraftServer
import requests
import pyautogui

requests_counter = 0
clicked = False
global response
settings = ["settings", "autoclick", "ping", "request-delay"]

def getSetting(settingName):
    try:
        file = open("settings.txt", "r+")
        for word in file:
            if(word.startswith(settingName)):
                file.close()
                return getValue(word.lower(), settingName)
        global val
        print("[ОШИБКА] Не удалось найти значение \"" + settingName + "\"! Создаём...")
        if(settingName == "request-delay" or settingName == "ping"):
            file.write(settingName + " = true\n")
            val = True
        else:
            file.write(settingName + " = false\n")
            val = False
        file.close()
        return val
    except:
        print("[ОШИБКА] Не удалось найти settings.txt! Создаём...")
        file = open("settings.txt", "w")
        file.write("https://github.com/ZimnyCat/jewtrick-client/wiki/JEW-TRICK-WIKI\n")
        file.close()
        return False

def getValue(word, setting):
    global result
    result = False
    if(word == setting + " = true\n"):
        result = True
    if (word == setting + " = false\n"):
        result = False
    return result

print("─╔╦═╦╦═╦╗╔══╦═╦══╦═╦╦╗")
print("─║║╦╣║║║║╚╗╔╣╬╠║║╣╔╣╔╝")
print("╔╣║╩╣║║║║─║║║╗╬║║╣╚╣╚╗")
print("╚═╩═╩═╩═╝─╚╝╚╩╩══╩═╩╩╝")
print("jew trick (client) v2.1\nhttps://jewtrick.ml")
print("")
motd = requests.get("https://jewtrick.ml/server/motdv21.html")
if motd.status_code == 200:
    print(motd.text + "\n")
for word in settings:
    getSetting(word)
if(getSetting("settings") == False):
    print("Вы можете настроить jew trick в файле settings.txt\n")
if(getSetting("autoclick") and getSetting("settings")):
    response = "да"
    print("AutoClick установлен на " + response + "\n")
elif(getSetting("settings") and getSetting("autoclick") == False):
    response = "нет"
    print("AutoClick установлен на " + response + "\n")
else:
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
    requests_counter += 1
    try:
        jew_int = int(requests.get("https://jewtrick.ml/server/jewtrickstatus.html").text)
        if jew_int == 2:
            request_delay = 2
            if(getSetting("request-delay") == False and getSetting("settings")):
                request_delay = 1
            jew_online = requests.get("https://jewtrick.ml/server/jew_online.html").text
            if(getSetting("ping") == False and getSetting("settings")):
                print("JEW TRICK TIME!!! Онлайн 2b2t:", jew_online)
                if response == "да" and clicked == False:
                    pyautogui.doubleClick(button="left")
                    clicked = True
            else:
                try:
                    online = MinecraftServer.lookup("2b2t.org").status().players.online
                    print("JEW TRICK TIME!!! Онлайн 2b2t (сервер jew trick):", jew_online, "Онлайн 2b2t (запрос):",
                          online, "(" + str(requests_counter) + ")")
                    if response == "да" and clicked == False:
                        pyautogui.doubleClick(button="left")
                        clicked = True
                except:
                    print("jew trick сейчас невозможен (" + str(requests_counter) + ")")
        elif jew_int == 1:
            print("jew trick сейчас невозможен (" + str(requests_counter) + ")")
            clicked = False
        elif jew_int == 0:
            print("2b2t не отвечает (" + str(requests_counter) + ")")
    except:
        if requests.get("https://jewtrick.ml/server/jewtrickstatus.html").status_code == 200:
            print("Сервер jew trick получает онлайн 2b2t (" + str(requests_counter) + ")")
        else:
            print("Сервер jew trick недоступен (" + str(requests_counter) + ")")
    sleep(request_delay)