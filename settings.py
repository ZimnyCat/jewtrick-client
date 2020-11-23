settings_list = ["settings", "autoclick", "ping", "request-delay"]

def getSetting(settingName):
    if not (settingName in settings_list):
        print("[ОШИБКА] Значение \"" + settingName + "\" не найдено в settings.settings_list!")
        return False
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