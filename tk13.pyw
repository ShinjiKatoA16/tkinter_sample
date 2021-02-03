# tk13.pyw
# modify to study git/github 2021/2/3

import tkinter as tk
root = tk.Tk()
root.geometry('400x200')
lb = tk.Label(text='This is a Label. This is a Label.\nThis is a Label.')
ms = tk.Message(text='This is a Message. This is a Message. This is a Message.')
[widget.pack() for widget in (lb,ms)]
root.mainloop()