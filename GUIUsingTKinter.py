import tkinter as tk
w=tk.Tk()
w.title("GUI Example")
w.geometry("600x400")
label=tk.Label(w,text="welcome to aimca,bhatkal by using tkinter")
label.pack()
button=tk.Button(w,text="click me",command=w.destroy)
button.pack()
w.mainloop()