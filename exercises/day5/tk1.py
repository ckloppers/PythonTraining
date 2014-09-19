from Tkinter import *

main = Tk()


def display():
    print name.get(), ':', age.get()


Label(main, text='Name').pack()
name = Entry(main,
             width=40)
name.pack()

Label(main, text='Age').pack()
age = Entry(main,
            width=40)
age.pack()

btn = Button(main,
       text='OK',
       command=display)
btn.pack()

main.mainloop()