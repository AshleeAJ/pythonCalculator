import tkinter as tk


def insert_entry(item):
    current = Entry.get()
    Entry.delete(0,tk.END)
    Entry.insert(0, current + item)


def clear():
    Entry.delete(0,tk.END)


def equals():
    result = eval(Entry.get())
    Entry.delete(0,tk.END)
    Entry.insert(0,result)

win = tk.Tk()
# win.geometry('150x150')
win.winfo_toplevel().title('calculator')

# Entry field
Entry = tk.Entry(win)

# Number buttons
B0 = tk.Button(win, text='0', command=lambda:insert_entry('0'))
B1 = tk.Button(win, text='1', command=lambda:insert_entry('1'))
B2 = tk.Button(win, text='2', command=lambda:insert_entry('2'))
B3 = tk.Button(win, text='3', command=lambda:insert_entry('3'))
B4 = tk.Button(win, text='4', command=lambda:insert_entry('4'))
B5 = tk.Button(win, text='5', command=lambda:insert_entry('5'))
B6 = tk.Button(win, text='6', command=lambda:insert_entry('6'))
B7 = tk.Button(win, text='7', command=lambda:insert_entry('7'))
B8 = tk.Button(win, text='8', command=lambda:insert_entry('8'))
B9 = tk.Button(win, text='9', command=lambda:insert_entry('9'))

# Function buttons
Plus = tk.Button(win, text='+', command=lambda:insert_entry('+'))
Minus = tk.Button(win, text='-', command=lambda:insert_entry('-'))
Times = tk.Button(win, text='*', command=lambda:insert_entry('*'))
Divide = tk.Button(win, text='/', command=lambda:insert_entry('/'))
Equals = tk.Button(win, text='=', command=lambda:equals())
Clear = tk.Button(win, text='C', command=lambda:clear())

# Entry field placement
Entry.grid(row=0, column=0, columnspan=4)

# Number placement
B0.grid(row=1, column=0, sticky='nsew')
B1.grid(row=1, column=1, sticky='nsew')
B2.grid(row=1, column=2, sticky='nsew')
B3.grid(row=2, column=0, sticky='nsew')
B4.grid(row=2, column=1, sticky='nsew')
B5.grid(row=2, column=2, sticky='nsew')
B6.grid(row=3, column=0, sticky='nsew')
B7.grid(row=3, column=1, sticky='nsew')
B8.grid(row=3, column=2, sticky='nsew')
B9.grid(row=4, column=0, sticky='nsew')

# Function placement
Plus.grid(row=1, column=3, sticky='nsew')
Minus.grid(row=2, column=3, sticky='nsew')
Times.grid(row=3, column=3, sticky='nsew')
Divide.grid(row=4, column=3, sticky='nsew')
Equals.grid(row=4, column=1, sticky='nsew')
Clear.grid(row=4, column=2, sticky='nsew')


win.mainloop()
