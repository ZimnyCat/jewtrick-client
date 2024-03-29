# -*- coding: utf-8 -*-

import utils.settings as s
import utils.system as sys


def check(settingName):
    if settingName not in s.numArray and settingName not in s.booleanArray:
        sys.crash("Значение \"{settingName}\" не найдено в setting.numArray или в setting.booleanArray!",
                  "Отправьте эту ошибку разработчику, от которого вы получили эту версию jew trick")


def createSettingsFile():
    file = open("settings.txt", "w")
    file.write("https://jewtrick.xyz/settings\n\n")
    for word in s.booleanArray:
        file.write(word + " = " + s.booleanArray[word] + "\n")
    for word in s.numArray:
        file.write(word + " = " + str(s.numArray[word]) + "\n")
    file.close()
    print("Вы можете настроить jew trick в settings.txt")
    return False
