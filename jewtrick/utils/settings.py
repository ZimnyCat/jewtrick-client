# -*- coding: utf-8 -*-

import utils.settingsHelper as helper
import utils.system as sys

booleanArray = {
    "autoclick": "false",
    "ping": "true",
    "time": "false",
    "requests-counter": "true"
}

numArray = {
    "delay": 1,
    "ping-delay": 5
}


def getBoolean(settingName):
    # проверяем
    if helper.check(settingName):
        return False
    try:
        file = open("settings.txt", "r+")
        # ищем настройку
        for word in file:
            nigga = settingName + " = "
            if word.startswith(nigga):
                file.close()
                if word == nigga + "true\n":
                    return True
                elif word == nigga + "false\n":
                    return False
                # если значение не булевое
                sys.crash("Настройка \"" + settingName + "\" не соответствует true или false",
                          "Проверьте ваш файл settings.txt")
        # если такая настройка не найдена в файле
        print("Не удалось найти значение \"" + settingName + "\"! Записываем...")
        file.write(settingName + " = " + booleanArray[settingName] + "\n")
        file.close()
        return getBoolean(settingName)
    except FileNotFoundError:
        # если файла settings.txt нет
        helper.createSettingsFile()
        return getBoolean(settingName)


def getNum(settingName):
    # проверяем
    helper.check(settingName)
    try:
        file = open("settings.txt", "r+")
        # ищем настройку
        for word in file:
            nigga = settingName + " = "
            if word.startswith(nigga):
                file.close()
                try:
                    return int(word.replace(nigga, ""))
                except:
                    # если значение не число
                    sys.crash("Настрйка \"" + settingName + "\" не является числом")
        # если такая настройка не найдена
        print("Не удалось найти значение \"" + settingName + "\"! Записываем...")
        file.write(settingName + " = " + str(numArray[settingName]) + "\n")
        file.close()
        return getNum(settingName)
    except:
        # если файла settings.txt нет
        helper.createSettingsFile()
        return getNum(settingName)
