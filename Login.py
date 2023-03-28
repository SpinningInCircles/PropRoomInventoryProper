#-----Importing-----
import tkinter as tk
from tkinter import messagebox
import json
import os
import re

mainWindow = tk.Tk()
mainWindow.title("Prop Room Inventory")

if os.path.getsize("./user_info.json") == 0:
    logInfo = dict()
    with open ("user_info.json", "w") as file:
        json.dump(logInfo, file)

winWidth = 600
winHeight = 400
scrWidth = mainWindow.winfo_screenwidth()
scrHeight = mainWindow.winfo_screenheight()
midX = int(scrWidth / 2 - winWidth / 2)
midY = int(scrHeight / 2 - winHeight / 2)

mainWindow.geometry(f"{winWidth}x{winHeight}+{midX}+{midY}")


def register():
    def addUserInfo(user, password):
        flag = 0
        user = user.get()
        password = password.get()
        f = open("user_info.json")
        logInfo = json.load(f)
        if user in logInfo:
            flag = -1
        elif (len(password) <= 8) or (not re.search("[A-Z]", password)) or (not re.search("[0-9]", password)) or (not re.search("[!@#$%^&*()-_=+/]", password)):
                flag = -1

        if flag != -1:
            messagebox.showinfo("Success", "Registered!")
            with open("user_info.json", "r+") as outfile:
                file_data = json.load(outfile)
                file_data.update({user:password})
                outfile.seek(0)
                json.dump(file_data, outfile, indent=4)
            regWindow.destroy()
            return

        else:
            messagebox.showinfo("Uh-oh", "Username or Password is invalid.")
            return
    regWindow = tk.Toplevel()
    regWindow.title("Registry")

    winWidth = 600
    winHeight = 400
    scrWidth = regWindow.winfo_screenwidth()
    scrHeight = regWindow.winfo_screenheight()
    midX = int(scrWidth / 2 - winWidth / 2)
    midY = int(scrHeight / 2 - winHeight / 2)

    regWindow.geometry(f"{winWidth}x{winHeight}+{midX}+{midY}")

    user = tk.StringVar()
    password = tk.StringVar()

    tk.Label(regWindow, text="Username").pack()
    user = tk.Entry(regWindow, textvariable=user)
    user.pack()
    tk.Label(regWindow, text="Password").pack()
    password = tk.Entry(regWindow, textvariable=password, show="*")
    password.pack()
    tk.Label(regWindow, text="Password must contain: A capital letter, a number, and a symbol").pack()

    tk.Button(regWindow, text="Register", command=lambda: addUserInfo(user, password)).pack()

    regWindow.mainloop()

def login():
    def findUser(user, password):
        user = user.get()
        password = password.get()
        success = None

        f = open("user_info.json")
        user_data = json.load(f)
        x = user_data.keys()

        for i in x:
            if user == i:
                success = True
                if user_data[user] == password:
                    messagebox.showinfo("Success!", "You've been logged in!")
                    logWindow.destroy()
                    mainWindow.destroy()
                    exec(open("PropInventory").read())
                else:
                    messagebox.showinfo("Oops!", "The password you've entered is incorrect :(")
        if not success:
            messagebox.showinfo("Oops!", "The username you entered is not registered :(")

    logWindow = tk.Toplevel()

    winWidth = 600
    winHeight = 400
    scrWidth = logWindow.winfo_screenwidth()
    scrHeight = logWindow.winfo_screenheight()
    midX = int(scrWidth / 2 - winWidth / 2)
    midY = int(scrHeight / 2 - winHeight / 2)

    logWindow.geometry(f"{winWidth}x{winHeight}+{midX}+{midY}")

    user = tk.StringVar()
    password = tk.StringVar()

    tk.Label(logWindow, text="Username").pack()
    user = tk.Entry(logWindow, textvariable=user)
    user.pack()
    tk.Label(logWindow, text="Password").pack()
    password = tk.Entry(logWindow, textvariable=password, show="*")
    password.pack()

    tk.Button(logWindow, text="Log-in",command=lambda:findUser(user,password)).pack()

    logWindow.mainloop()


tk.Button(mainWindow, text="Log-in", bd="5", command=login).pack()
tk.Button(mainWindow, text="Register", bd="5", command=register).pack()
mainWindow.mainloop()
