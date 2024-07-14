from tkinter import *
from datetime import * 

dt = datetime.now()
hr = dt.hour
if hr < 12:
	msg = "Good Morning"
elif hr < 16:
	msg = "Good Afternoon"
else:
	msg = "Good evening"

root = Tk()
root.title("App by Harshvardhan")
root.geometry("800x300+100+50")
f = ("times new roman", 80, "bold", "italic")
lab = Label(root, text=msg, font=f, fg="dark orange")
lab.pack(pady=20)

root.mainloop()