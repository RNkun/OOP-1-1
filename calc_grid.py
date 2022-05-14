from tkinter import *

window =Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

class MyWindow:
    def __init__(self, window):
        #Input values and Title
        self.lbl1 = Label(window, text="Simple Calculator", font="Stencil 20 bold italic")
        self.lbl1.grid(row=0, column=0, sticky='WE', columnspan=2)
        self.lbl2 = Label(window, text="Enter the 1st Number:", font="Times 12 underline")
        self.lbl2.grid(row=1, column=0)
        self.txt2 =Entry(window, bd=3, font="Times 12")
        self.txt2.grid(row=1, column=1)
        self.lbl3 = Label(window, text="Enter the 2nd Number", font="Times 12 underline")
        self.lbl3.grid(row=2, column=0)
        self.txt3 = Entry(window, bd=3, font="Times 12")
        self.txt3.grid(row=2, column=1)

        #operation button
        self.btn1 = Button(window, text="Add", fg="green", font="Stencil 10 italic")
        self.btn1.grid(row=4, column=0)
        self.btn1.bind('<Button 1>', self.add)
        self.btn2 = Button(window, text="Subtract", fg="green", font="Stencil 10 italic")
        self.btn2.grid(row=4, column=1)
        self.btn2.bind('<Button 1>', self.subtract)
        self.btn3 = Button(window, text="Multiply", fg="green", font="Stencil 10 italic")
        self.btn3.grid(row=5, column=0)
        self.btn3.bind('<Button 1>', self.multiply)
        self.btn4 = Button(window, text="Divide", fg="green", font="Stencil 10 italic")
        self.btn4.grid(row=5, column=1)
        self.btn4.bind('<Button 1>', self.divide)

        #result label
        self.lbl4 = Label(window, text="Result", font="Times 12 underline")
        self.lbl4.grid(row=6, column=0)
        self.txt4 = Entry(window, bd=3, font="Times 12 bold italic", fg="red")
        self.txt4.grid(row=6, column=1)

    #operations
    def add(self, event):
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 + num2
        self.txt4.insert(END, str(answer))

    def subtract(self, event):
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 - num2
        self.txt4.insert(END, str(answer))

    def multiply(self, event):
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 * num2
        self.txt4.insert(END, str(answer))

    def divide(self, event):
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 / num2
        self.txt4.insert(END, str(answer))


mywin = MyWindow(window)


window.mainloop()