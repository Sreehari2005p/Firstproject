import tkinter
from tkinter import messagebox,ttk
from tkinter import PhotoImage
from openpyxl import load_workbook

root=tkinter.Tk()
#   image_path=PhotoImage(file=r"C:\Users\Nijil\OneDrive\Desktop\plan\PIC1.bmp")
File_Path=r"C:\Users\Nijil\OneDrive\Desktop\Data Science\Book1.xlsx"

A=load_workbook(File_Path)
B=A["Registration"]
def On_Click_Submit():
    name=Name_Tbox.get()
    email=Email_Tbox.get()
    phone=Ph_Tbox.get() 
    Branch=Branch_Dropdown.get()
    chkval=agree_value.get()

    if name and email and phone and Branch and chkval==1:
        B.append([name,email,phone,Branch,'Yes'])
        A.save(File_Path)   
        messagebox.showinfo("Status","Data Submitted")
    else:
        messagebox.showwarning("Warning","Pls fill All the field")

root.geometry("300x300")
root.title("Registration Form")
root.configure(bg="#ffcccb")
Lbl_=tkinter.Label(root,text="Registration  Form")
Lbl_.configure(bg="#ffcccb")
Lbl_.pack()
Lbl_Name=tkinter.Label(root,text="Enter Name")
Lbl_Name.pack(anchor=tkinter.W,padx=20)
Lbl_Name.configure(bg="#ffcccb")

Name_Tbox=tkinter.Entry(root)
Name_Tbox.pack(anchor=tkinter.W,padx=20)

Lbl_Email=tkinter.Label(root,text="Enter Email")
Lbl_Email.pack(anchor=tkinter.W,padx=20)
Lbl_Email.configure(bg="#ffcccb")

Email_Tbox=tkinter.Entry(root)
Email_Tbox.pack(anchor=tkinter.W,padx=20)

Lbl_ph=tkinter.Label(root,text="Enter Phone")
Lbl_ph.pack(anchor=tkinter.W,padx=20)
Lbl_ph.configure(bg="#ffcccb")

Ph_Tbox=tkinter.Entry(root)
Ph_Tbox.pack(anchor=tkinter.W,padx=20)

Branch_Label=tkinter.Label(root,text="Select branch")
Branch_Label.pack(anchor=tkinter.W,padx=20)
Branch_Label.configure(bg="#ffcccb")


choices=['CS','EC','ME']
Branch_Dropdown=ttk.Combobox(root,values=choices)
Branch_Dropdown.pack(anchor=tkinter.W,padx=20)

Lbl_1=tkinter.Label(root,text=" ")
Lbl_1.configure(bg="#ffcccb")
Lbl_1.pack()
# Checkbox
agree_value=tkinter.IntVar() # uncheck =0,check=1
agree_checkbox=ttk.Checkbutton(root,text="Do You Agree With Terms&Condition",variable=agree_value)

agree_checkbox.pack(anchor=tkinter.W,padx=20,pady=5)

Submit_button=tkinter.Button(root,text="Submit",command=On_Click_Submit)
Submit_button.pack(anchor=tkinter.W,pady=5,padx=30)

root.mainloop()
