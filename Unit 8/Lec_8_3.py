from tkinter import *

root = Tk()

root['bg'] = 'light yellow'

status = Frame(root)
status['bg'] = 'light green'

ID1 = Label(status)
ID1['text'] = 'Status frame'
ID1['bg'] = 'light blue'
ID1.pack()

action = Frame(root)
action['bg'] = 'pink'

ID2 = Label(action)
ID2['text'] = 'Action frame'
ID2['bg'] = 'light blue'
ID2.pack()

#status.pack()
status.pack(expand=YES, fill=BOTH)
action.pack()

mainloop()
