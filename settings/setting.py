import settings.utils as utils

booleanArray = ["autoclick", "ping", "time"]
numArray = ["delay"]


def getBoolean(settingName):
    # проверяем
    if utils.check(settingName):
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
                utils.crash("Настрйка \"" + settingName + "\" не соответствует true или false")
        # если такая настройка не найдена в файле
        print("Не удалось найти значение \"" + settingName + "\"! Записываем...")
        file.write(settingName + " = false\n")
        file.close()
        return False
    except FileNotFoundError:
        # если файла settings.txt нет
        utils.createSettingsFile()
        return False


def getNum(settingName):
    # проверяем
    utils.check(settingName)
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
                    utils.crash("Настрйка \"" + settingName + "\" не является числом")
        # если такая настройка не найдена
        print("Не удалось найти значение \"" + settingName + "\"! Записываем...")
        file.write(settingName + " = 1\n")
        file.close()
        return 1
    except:
        # если файла settings.txt нет
        utils.createSettingsFile()
