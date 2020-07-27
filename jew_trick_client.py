from time import sleep
import requests

requests_counter = 0
print("─╔╦═╦╦═╦╗╔══╦═╦══╦═╦╦╗")
print("─║║╦╣║║║║╚╗╔╣╬╠║║╣╔╣╔╝")
print("╔╣║╩╣║║║║─║║║╗╬║║╣╚╣╚╗")
print("╚═╩═╩═╩═╝─╚╝╚╩╩══╩═╩╩╝")
print("jew trick (client) v1.2")
print("https://jewtrick.ml")
print("")
motd = requests.get("https://jewtrick.ml/server/motdv11.html")
if motd.status_code == 200:
    print(motd.text)
print("")
while True:
    requests_counter = requests_counter + 1
    try:
        jew_int = int(requests.get("https://jewtrick.ml/server/jewtrickstatus.html").text)
        if jew_int == 2:
            jew_online = requests.get("https://jewtrick.ml/server/jew_online.html").text
            print("JEW TRICK TIME!!! Онлайн 2b2t:", jew_online, "(" + str(requests_counter) + ")")
        elif jew_int == 1:
            print("jew trick сейчас невозможен (" + str(requests_counter) + ")")
        elif jew_int == 0:
            print("2b2t не отвечает (" + str(requests_counter) + ")")
    except:
        if requests.get("https://jewtrick.ml/server/jewtrickstatus.html").status_code == 200:
            print("Сервер jew trick получает онлайн 2b2t (" + str(requests_counter) + ")")
        else:
            print("Сервер jew trick недоступен (" + str(requests_counter) + ")")
    sleep(1)