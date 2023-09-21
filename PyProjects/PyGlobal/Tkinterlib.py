import tkinter
root=tkinter.Tk()
root.title("Registration Form")

name_label=tkinter.Label(root,text="Enter name")
name_label.pack()
name_textbox=tkinter.Entry(root)
name_textbox.pack()

Email_label=tkinter.Label(root,text="Enter Email")
Email_label.pack()
Email_textbox=tkinter.Entry(root)
Email_textbox.pack()

Phone_label=tkinter.Label(root,text="Enter Phone Number")
Phone_label.pack()
Phone_textbox=tkinter.Entry(root)
Phone_textbox.pack()

submit_button=tkinter.Button(root,text="Submit")
submit_button.pack()

root.mainloop()