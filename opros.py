from tkinter import *
from tkinter import messagebox
import random

while True:
    def Da():
        messagebox.showinfo('', 'Осуждаю')
        quit()

    def Motion(event):
        bt2.place(x=random.randint(0,300), y=random.randint(0,300))

    window = Tk()
    window.title("Опрос")
    window.geometry("400x400")
    l1 = Label(window, text='С++ имба?', font=("Arial", 20))
    l1.pack()
    bt1 = Button(width=5, bd=5, text='Да', command=Da)
    bt1.place(x=50, y=200)
    bt2 = Button(width=5, bd=5, text='Нет',)
    bt2.place(x=300, y=200)
    bt2.bind('<Enter>', Motion)
    window.mainloop()
    