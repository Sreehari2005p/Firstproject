import tkinter
root=tkinter.Tk()
root.geometry("300x200")
root.configure(bg="#ffcccb")

root.title("Registration Form")

name_label=tkinter.Label(root,text="Enter name")
name_label.configure(bg="#ffcccb")
name_label.pack(anchor=tkinter.W,padx=10)
name_textbox=tkinter.Entry(root)
name_textbox.pack(anchor=tkinter.W,padx=10)

Email_label=tkinter.Label(root,text="Enter Email")
Email_label.configure(bg="#ffcccb")
Email_label.pack(anchor=tkinter.W,padx=10)
Email_textbox=tkinter.Entry(root)
Email_textbox.pack(anchor=tkinter.W,padx=10)

Phone_label=tkinter.Label(root,text="Enter Phone Number")
Phone_label.configure(bg="#ffcccb")
Phone_label.pack(anchor=tkinter.W,padx=10)
Phone_textbox=tkinter.Entry(root)
Phone_textbox.pack(anchor=tkinter.W,padx=10)

submit_button=tkinter.Button(root,text="Submit")
submit_button.pack(anchor=tkinter.W,padx=10)

root.mainloop()