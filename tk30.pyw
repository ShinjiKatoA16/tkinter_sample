# P19 tk30.pyw under git control

import tkinter as tk

def get_ckval():
    if boolvar.get():
        lb['text'] = 'チェックされている'
    else:
        lb['text'] = 'チェックされていない'


root = tk.Tk()
root.geometry('250x100')
boolvar = tk.BooleanVar()
lb = tk.Label()
ck = tk.Checkbutton(text='チェックボックス', variable=boolvar)
bt = tk.Button(text='判定', command=get_ckval)
[widget.pack() for widget in (lb,ck,bt)]

root.mainloop()