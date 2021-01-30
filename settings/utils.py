import settings.setting as s
from datetime import datetime


def check(settingName):
    if settingName not in s.numArray and settingName not in s.booleanArray:
        crash(f"Значение \"{settingName}\" не найдено в setting.numArray или в setting.booleanArray!")


def createSettingsFile():
    file = open("settings.txt", "w")
    file.write("https://github.com/ZimnyCat/jewtrick-client/wiki/JEW-TRICK-WIKI\n")
    for word in s.booleanArray:
        file.write(word + " = false\n")
    for word in s.numArray:
        file.write(word + " = 1\n")
    file.close()
    print("Вы можете настроить jew trick в settings.txt")
    return False


def crash(reason):
    file = open(str("crash-" + datetime.today().strftime("%Y-%m-%d-%H-%M-%S") + ".txt"), "w")
    file.write("[ОШИБКА] " + reason + "\nОтправьте эту ошибку разработчику, от которого вы получили эту версию jew trick")
    file.close()
    exit(1)
