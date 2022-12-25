from tkinter import *
import tkinter



window = Tk()
window.title("Spell Correction")
window.geometry("800x600")

label1 = Label(window, font=('Times New Roman',12), text='Phát hiện và sửa lỗi chính tả')
label1.place(x = 10, y = 10)
txt = Entry(window, width=100, font=('Times New Roman',12))
txt.place(x=30, y=30)
def nhapVao():
    label2 = Label(window, font=('Times New Roman',12), text='Câu sau khi chỉnh : ' + txt.get())
    label2.place(x=60,y=50)
button = Button(window, text='Sửa', width=10, height=1, font=('Times New Roman',12), command=nhapVao)
button.place(x=90,y=90)


window.mainloop()