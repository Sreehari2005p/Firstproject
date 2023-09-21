import tkinter
root=tkinter.Tk()

name_label=tkinter.Label(root,text="Enter name")
name_label.pack()
name_textbox=tkinter.Entry(root)
name_textbox.pack()

Email_label=tkinter.Label(root,text="Enter Email")
Email_label.pack()
Email_textbox=tkinter.Entry(root)
Email_textbox.pack()

root.mainloop()