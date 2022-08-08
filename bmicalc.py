import tkinter as tk
from tkinter import *
import tkinter.messagebox


def resetValueToZero():
    height.delete(0, END)
    weight.delete(0, END)


def bmiCalculator():
    heightVal = float(height.get())
    weightVal = float(weight.get())
    heightInMetre = heightVal / 100
    bmiIndex = round(weightVal / ((heightInMetre) ** 2), 2)
    bmiMessage(bmiIndex)


def bmiMessage(bmiIndex):
    if bmiIndex < 18.5:
        tkinter.messagebox.showinfo(
            'BMI Message', f'BMI = {bmiIndex} is underweight')
    elif (bmiIndex > 18.5) and (bmiIndex < 24.9):
        tkinter.messagebox.showinfo(
            'BMI Message', f'BMI = {bmiIndex} is normal')
    elif (bmiIndex > 24.9) and (bmiIndex < 29.9):
        tkinter.messagebox.showinfo(
            'BMI Message', f'BMI = {bmiIndex} is overweight')
    elif (bmiIndex > 29.9):
        tkinter.messagebox.showinfo(
            'BMI Message', f'BMI = {bmiIndex} is obesity')
    else:
        tkinter.messagebox.showerror('BMI Message', 'Invalid input!')


if __name__ == '__main__':
    # instantiate the window
    window = tk.Tk()

    var = IntVar()

    # design the title and box size
    window.title('BMI Calculator')
    window.geometry('300x150')

    frame = Frame(window, padx=10, pady=10)
    frame.pack()

    # height label
    heightLabel = Label(frame, text='Enter the height in cm: ')
    heightLabel.grid(row=3, column=1)
    height = tk.Entry(frame)
    height.grid(row=3, column=2, pady=5)

    # weight label
    weightLabel = Label(frame, text='Enter the weight in kg: ')
    weightLabel.grid(row=4, column=1)
    weight = tk.Entry(frame)
    weight.grid(row=4, column=2, pady=5)

    frameTwo = Frame(frame)
    frameTwo.grid(row=5, columnspan=3, pady=10)

    # instantiate calculate button
    calculateButton = Button(frameTwo, text='Calculate', command=bmiCalculator)
    calculateButton.pack(side=LEFT)

    # delete the value
    deleteButton = Button(frameTwo, text='Delete', command=resetValueToZero)
    deleteButton.pack(side=LEFT)

    # window showup
    window.mainloop()


# ---------------------------------------------------------------------
# This code was adapted from pythonguides.com and has been modified.                                                                                                       
# source: https://pythonguides.com/bmi-calculator-using-python-tkinter/
