import json
import re
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Prop Room Inventory")

logInfo = dict()

winWidth = 600
winHeight = 400
scrWidth = mainWindow.winfo_screenwidth()
scrHeight = mainWindow.winfo_screenheight()
midX = int(scrWidth / 2 - winWidth / 2)
midY = int(scrHeight / 2 - winHeight / 2)

mainWindow.geometry(f"{winWidth}x{winHeight}+{midX}+{midY}")


def register():
    def addUserInfo(user, password):
        def saveUserInfo():
            with open("user_info.json", "w") as info:
                json.dump(logInfo, info)

        flag = 0
        user = user.get()
        password = password.get()
        for key in logInfo:
            if key == user:
                flag = -1
                break
            else:
                for i in password:
                    if (len(password) <= 8):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", password):
                        flag = -1
                        break
                    elif not re.search("[0-9]", password):
                        flag = -1
                        break
                    elif re.search("[!@#$%^&*()-_=+/]", password):
                        flag = -1
                        break
                    elif re.search("\s", password):
                        flag = -1
                        break
        if flag != -1:
            regText.set("Registered :)")
            logInfo[user] = password
            saveUserInfo()
            return

        else:
            regText.set("Invalid Username or Password :(")
            return
    regWindow = tk.Tk()
    regWindow.title("Registry")

    winWidth = 600
    winHeight = 400
    scrWidth = regWindow.winfo_screenwidth()
    scrHeight = regWindow.winfo_screenheight()
    midX = int(scrWidth / 2 - winWidth / 2)
    midY = int(scrHeight / 2 - winHeight / 2)

    regWindow.geometry(f"{winWidth}x{winHeight}+{midX}+{midY}")
    
    regText =tk.StringVar()
    user = tk.StringVar()
    password = tk.StringVar()

    user = tk.Entry(regWindow, textvariable=user)
    user.pack()
    password = tk.Entry(regWindow, textvariable=password)
    password.pack()

    tk.Button(regWindow, text="Register", command=lambda: addUserInfo(user, password)).pack()
    tk.Label(regWindow, textvariable=regText).pack()

    regWindow.mainloop()


tk.Button(mainWindow, text="Register", bd="5", command=register).pack()
mainWindow.mainloop()
