from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window, text="Standard Calculator")
        self.lbl1.place(relx=0.50, y=50, anchor="center")
        self.lbl2 = Label(window, text="Input the 1st Number")
        self.lbl2.place(x=50, y=80)
        self.txt2 = Entry(window, bd=3)
        self.txt2.place(x= 180, y=80)
        self.lbl3 = Label(window, text="Input the 2nd Number")
        self.lbl3.place(x=50, y=120)
        self.txt3 = Entry(window, bd=3)
        self.txt3.place(x=180, y=120)

        self.btn1 = Button(window, text="Add")
        self.btn1.place(x=50, y=150)
        self.btn1.bind('<Button 1>', self.add)
        self.btn2 = Button(window, text="Subtract")
        self.btn2.place(x=100, y=150)
        self.btn2.bind('<Button 1>', self.subtract)
        self.btn3 = Button(window, text="Multiply")
        self.btn3.place(x=175, y=150)
        self.btn3.bind('<Button 1>', self.multiply)
        self.btn4 = Button(window, text="Divide")
        self.btn4.place(x=250, y=150)
        self.btn4.bind('<Button 1>', self.divide)

        self.lbl4 = Label(window, text="Result")
        self.lbl4.place(x=50, y=200)
        self.txt4 = Entry(window, bd=3)
        self.txt4.place(x=120, y=200)

    def add(self, event):
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1+num2
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