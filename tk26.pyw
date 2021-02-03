# tk26

import tkinter as tk
def print_selpoint():
    sel_start=tx.index('sel.first')
    sel_end=tx.index('sel.last')
    print(tx.get(sel_start, sel_end))

root = tk.Tk()
tx = tk.Text(width=30, height=5)
bt = tk.Button(text='print selected area', command=print_selpoint)
[widget.pack() for widget in (tx,bt)]

root.mainloop()