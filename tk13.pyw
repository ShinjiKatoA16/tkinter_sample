# tk13.pyw

import tkinter as tk
root = tk.Tk()
root.geometry('350x250')
lb = tk.Label(text='This is a Label. This is a Label.\nThis is a Label.')
ms = tk.Message(text='This is a Message. This is a Message. This is a Message.')
[widget.pack() for widget in (lb,ms)]
root.mainloop()