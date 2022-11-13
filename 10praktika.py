from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import scrolledtext

def clicked1():
    def add_digit(digit):
        temp = calc.get()
        if temp[0] == '0' and len(temp) == 1:
            temp = temp[1:]
        calc.delete(0, END)
        calc.insert(0, temp + digit)

    def add_operation(operation):
        temp = calc.get()
        if temp[-1] in '-+/*':
            temp = temp[:-1]
        calc.delete(0, END)
        calc.insert(0, temp + operation)

    def calculate():
        temp = calc.get()
        if temp[-1] in '+-/*':
            temp = temp + temp[:-1]
        calc.delete(0, END)
        calc.insert(0, eval(temp))

    def clear():
        calc.delete(0, END)
        calc.insert(0, '0')

    def add_digit_button(digit):
        return Button(calculator_window, text=digit, bd=5, font=('Times New Roman', 13),
                      command=lambda: add_digit(digit))

    def add_operation_button(operation):
        return Button(calculator_window, text=operation, bd=5, font=('Times New Roman', 13),
                      command=lambda: add_operation(operation))

    def add_calc_button(operation):
        return Button(calculator_window, text=operation, bd=5, font=('Times New Roman', 13),
                      command=calculate)

    def add_clear_button(operation):
        return Button(calculator_window, text=operation, bd=5, font=('Times New Roman', 13),
                      command=clear)

    calculator_window = Tk()
    calculator_window.geometry('240x280+100+200')
    calculator_window.resizable(False, False)
    calculator_window.title('Calculator')
    calc = Entry(calculator_window, justify=RIGHT, font=('Times New Roman', 15), width=15)
    calc.insert(0, '0')
    calc.grid(column=0, row=0, columnspan=4, stick='wesn', padx=5)
    add_digit_button('1').grid(row=1, column=0, stick='wesn', padx=5, pady=5)
    add_digit_button('2').grid(row=1, column=1, stick='wesn', padx=5, pady=5)
    add_digit_button('3').grid(row=1, column=2, stick='wesn', padx=5, pady=5)
    add_digit_button('4').grid(row=2, column=0, stick='wesn', padx=5, pady=5)
    add_digit_button('5').grid(row=2, column=1, stick='wesn', padx=5, pady=5)
    add_digit_button('6').grid(row=2, column=2, stick='wesn', padx=5, pady=5)
    add_digit_button('7').grid(row=3, column=0, stick='wesn', padx=5, pady=5)
    add_digit_button('8').grid(row=3, column=1, stick='wesn', padx=5, pady=5)
    add_digit_button('9').grid(row=3, column=2, stick='wesn', padx=5, pady=5)
    add_digit_button('0').grid(row=4, column=0, stick='wesn', padx=5, pady=5)
    add_operation_button('+').grid(row=1, column=3, stick='wesn', padx=5, pady=5)
    add_operation_button('-').grid(row=2, column=3, stick='wesn', padx=5, pady=5)
    add_operation_button('*').grid(row=3, column=3, stick='wesn', padx=5, pady=5)
    add_operation_button('/').grid(row=4, column=3, stick='wesn', padx=5, pady=5)

    add_calc_button('=').grid(row=4, column=2, stick='wesn', padx=5, pady=5)
    add_clear_button('C').grid(row=4, column=1, stick='wesn', padx=5, pady=5)

    calculator_window.grid_columnconfigure(0, minsize=60)
    calculator_window.grid_columnconfigure(1, minsize=60)
    calculator_window.grid_columnconfigure(2, minsize=60)
    calculator_window.grid_columnconfigure(3, minsize=60)
    calculator_window.grid_rowconfigure(1, minsize=60)
    calculator_window.grid_rowconfigure(2, minsize=60)
    calculator_window.grid_rowconfigure(3, minsize=60)
    calculator_window.grid_rowconfigure(4, minsize=60)
    calculator_window.mainloop()


def open_info1():
    showinfo(title="Информация", message='Вы выбрали первый вариант')


def open_info2():
    showinfo(title="Информация", message='Вы выбрали второй вариант')


def open_info3():
    showinfo(title="Информация", message='Вы выбрали третий вариант')


window = Tk()
window.geometry('800x400')
btn1 = Button(window, text='Калькулятор', command=clicked1)
btn2 = Button(window, text='Первый', command=open_info1)
btn3 = Button(window, text='Второй', command=open_info2)
btn4 = Button(window, text='Третий', command=open_info3)
btn1.grid(column=2, row=0)
btn2.grid(column=3, row=0)
btn3.grid(column=4, row=0)
btn4.grid(column=5, row=0)

text = scrolledtext.ScrolledText(window, width=50, height=10, bg="white", fg="black")


def clicked2():
    with open('text.txt', 'r') as file:
        text.delete(1.0, END)
        text.insert(1.0, file.read())
    file.close()


def clicked3():
    with open('text.txt', 'w') as file1:
        file1.write(text.get(1.0, END))
    file1.close()


text.grid(row=0, column=0, columnspan=2, padx=35)
button2 = Button(window, text="Загузить", command=clicked2)
button2.grid(row=1, column=3, pady=10)
button3 = Button(window, text="Сохранить", command=clicked3)
button3.grid(row=1, column=4)
window.mainloop()
