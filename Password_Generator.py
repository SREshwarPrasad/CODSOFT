#importing essential modules
import tkinter as tk
import string
import random
from tkinter import messagebox


#initialising the root window
root= tk.Tk()
root.title("Password Generator")


#copy password to clipboard
def copy_password():
    root.clipboard_clear()  # Clear the clipboard
    copied_pwd = l_entry2.get()
    if copied_pwd != "":
        root.clipboard_append(l_entry2.get())  # Append the password to the clipboard
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Copy Error","No Password Copied")


#specifying the password length and displaying it
def password_length():
    l=l = [i for i in string.ascii_letters] + [i for i in "0123456789"] + [i for i in "\!@#$%^&*()_+-={}[]|:;<>?,./\"\'\\"]
    random.shuffle(l)
    s=""
    try:
        k = int(l_entry1.get())
        if k<=0:
            messagebox.showerror("Insufficient Length","Invalid length. Please try again! ")
            return
        if k<=8:
            ok = messagebox.showerror("Insufficient Length", "Length Insufficient for a strong password. Do you want to continue? ")
            if ok:
                for i in range(k):
                    s+=l[random.randrange(0,len(l))]
                l_entry2.config(state=tk.NORMAL)
                l_entry2.delete(0, tk.END)  
                l_entry2.insert(0, s)
                l_entry2.config(state="readonly")
                return  
        else:
            for i in range(k):
                s+=l[random.randrange(0,len(l))]
            l_entry2.config(state=tk.NORMAL)
            l_entry2.delete(0, tk.END)  
            l_entry2.insert(0, s)
            l_entry2.config(state="readonly")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid number!")


bg_color = "#e6f0ff"


#title
l1 = tk.Label(root, text = "PASSWORD  GENERATOR ", font = ("Georgia", 15, "bold"),bg=bg_color)
l1.place(x=143, y=15)


#length field
l2 = tk.Label(root, text = "Password Length: ",bg =bg_color)
l2.place(x=45, y=81)
l_entry1 = tk.Entry(root, width=50)
l_entry1.place(x=190, y=82)


#generated password field
l3 = tk.Label(root, text = "Generated Password: ", bg=bg_color)
l3.place(x =45, y =135)
l_entry2 = tk.Entry(root, width=50, state = "readonly")
l_entry2.place(x=190, y=135)


#generate button
gen_Button = tk.Button(root, text = "Generate", command = password_length, bg="#0066ff", fg="white", width=12)
gen_Button.place(x=150, y=200)


#copy the password generated
copy_pwd = tk.Button(root, text = "Copy Password", command = copy_password, bg="#0066ff", fg="white", width=12)
copy_pwd.place(x=315, y=200)


#background color 
root.configure(bg=bg_color)


#window size
root.geometry("557x260")
root.mainloop()

