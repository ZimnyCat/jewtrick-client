# -*- coding: utf-8 -*-

import utils.settings as s
import utils.system as sys


def check(settingName):
    if settingName not in s.numArray and settingName not in s.booleanArray:
        sys.crash("Значение \"{settingName}\" не найдено в setting.numArray или в setting.booleanArray!",
                  "Отправьте эту ошибку разработчику, от которого вы получили эту версию jew trick")


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
