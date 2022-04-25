#Problem 1: Modify the program below by adding two conversion methods - Fahrenheit to Celsius and Kelvin to Celsius

class TemperatureConversion:
    def __init__(self, temp):
        self.temp = temp


class CelsiusToFahrenheit(TemperatureConversion):
    def conversion(self):
        return (self.temp *9)/5 +32


class CelsiusToKelvin(TemperatureConversion):
    def conversion(self):
        return self.temp + 273.15


tempIn_CelToFah = CelsiusToFahrenheit(int(input("Celsius to Fahrenheit: Enter the Temperature in Celsius: ")))
print(tempIn_CelToFah.conversion())

tempIn_CelToKel = CelsiusToKelvin(int(input("Celsius to Kelvin: Enter the Temperature in Celsius: ")))
print(tempIn_CelToKel.conversion())

#Problem 2

from tkinter import *
window = Tk()

window.geometry("550x280+30+20")
window.title("Midterm in OOP")

fn = Label(window, text="Enter your Fullname", fg="Red")
fn.place(x=50, y=100)
fnbox = Entry(window, bd = 4, font = ("verdana",13))
fnbox.place(x=250, y=100)

def Display():
    dfn = Label(window, text=fnbox.get(), bd=4, font = ("verdana", 13))
    dfn.place(x=250, y=150)

displayButton = Button(window, text="Click to display your fullname", padx=4, pady=3, command=Display, fg="red")
displayButton.place(x=50, y=150)

window.mainloop()
