import utils.settings as s
from datetime import datetime
import pyautogui


def sendMsg(text, rc):
    print(_time() + text + " (" + str(rc) + ")")


def _time():
    if s.getBoolean("time"):
        return str("[" + datetime.today().strftime("%H:%M:%S") + "] ")
    else:
        return ""


def click(val):
    if s.getBoolean("autoclick") and not val:
        pyautogui.click(button="left")
        return True
    return val


def crash(reason, msg):
    file = open(str("crash-" + datetime.today().strftime("%Y-%m-%d-%H-%M-%S") + ".txt"), "w")
    file.write("[ОШИБКА] " + reason + "\n" + msg)
    file.close()
    exit(1)
