from tkinter import *
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Моё приложение")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
tk.iconbitmap("Без-названия.ico")

canvas = Canvas(tk,width = 700, height = 700, bg="blue", highlightthickness = 0)
canvas.pack()

canvas.create_oval(100,100,300,300,fill = "yellow",outline="")
canvas.create_oval(120,120,280,280,fill = "white", outline="red")

canvas.create_rectangle(400,100,500,700, fill = "lightgreen")
canvas.create_rectangle(420,120,480,480, fill = "darkgreen", outline="")
canvas.create_text(200,500, text="Hello,world!", font = ("Arial", 40), fill="white")
tk.mainloop()
