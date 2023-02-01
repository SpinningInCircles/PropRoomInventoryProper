import json
import tkinter as tk
import re

logInfo = dict()

mainWindow = tk.Tk()
mainWindow.title("Prop Room Inventory")

winWidth = 600
winHeight = 400
scrWidth = mainWindow.winfo_screenwidth()
scrHeight = mainWindow.winfo_screenheight()
midX = int(scrWidth / 2 - winWidth / 2)
midY = int(scrHeight / 2 - winHeight / 2)

mainWindow.geometry(f"{winWidth}x{winHeight}+{midX}+{midY}")

def addUserInfo(username, pw):
    flag = 0
    for i in pw:
        if (len(pw)<=8):
            flag = -1
            break
        elif not re.search("[A-Z]", pw):
            flag = -1
            break
        elif not re.search("[0-9]", pw):
            flag = -1
            break
        elif re.search("[!@#$%^&*()-_=+/]", pw):
            flag = -1
            break
        elif re.search("\s", pw):
            flag = -1
            break
    if flag == -1:
        passFail = "Invalid Password :("
    else:
        logInfo[username] = pw
        return



def register():
    regWindow = tk.Tk()
    regWindow.title("Registry")

    winWidth = 600
    winHeight = 400
    scrWidth = regWindow.winfo_screenwidth()
    scrHeight = regWindow.winfo_screenheight()
    midX = int(scrWidth / 2 - winWidth / 2)
    midY = int(scrHeight / 2 - winHeight / 2)

    regWindow.geometry(f"{winWidth}x{winHeight}+{midX}+{midY}")

    username = tk.Entry(regWindow).pack()
    pw = tk.Entry(regWindow).pack()

    tk.Button(regWindow, text = "register", command = addUserInfo(username, pw)).pack()
    passFail = tk.StringVar()
    passLabel = (regWindow, textvariable==passFail).pack()

    regWindow.mainloop()

regOpen = tk.Button(mainWindow, text = "register", bd = "5", command = register).grid(row = 2)
mainWindow.mainloop()