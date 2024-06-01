from tkinter import *

window = Tk()
window.title("Welcome to PomoDoro app")

canvas = Canvas(window, width=300, height=300)
pomodoro_img = PhotoImage(file=r"D:\sankhu codes and stuff\angela yu course\python\pomodoro1.py\tomato.png")

canvas.create_image(150, 150, image=pomodoro_img)
canvas.pack()

window.mainloop()
