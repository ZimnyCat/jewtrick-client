import settings.setting as s


def check(settingName):
    if settingName not in s.numArray and settingName not in s.booleanArray:
        print(f"[ОШИБКА] Значение \"{settingName}\" не найдено в setting.numArray или в setting.booleanArray!")
        return True


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
