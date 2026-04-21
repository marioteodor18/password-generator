import tkinter as tk
import random
import string

def generate_password():
    length = length_slider.get()
    
    chars = ""
    if var_upper.get():   chars += string.ascii_uppercase
    if var_lower.get():   chars += string.ascii_lowercase
    if var_digits.get():  chars += string.digits
    if var_special.get(): chars += string.punctuation

    if not chars:
        result_var.set("Selecteaza cel putin o optiune!")
        return

    password = ""
    for i in range(length):
        password += random.choice(chars)

    result_var.set(password)

def copy_password():
    pwd = result_var.get()
    if not pwd or pwd == "Selecteaza cel putin o optiune!":
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    copy_btn.config(text="Copiat!")
    root.after(1500, lambda: copy_btn.config(text="Copiaza"))


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x320")
root.resizable(False, False)
root.config(bg="#f0f0f0")


tk.Label(root, text="Password Generator",
         font=("Helvetica", 16, "bold"),
         bg="#f0f0f0").pack(pady=(20, 4))

tk.Label(root, text="Genereaza o parola sigura",
         font=("Helvetica", 9),
         fg="gray", bg="#f0f0f0").pack()


tk.Label(root, text="Lungime parola:",
         font=("Helvetica", 10),
         bg="#f0f0f0").pack(pady=(16, 0))

length_slider = tk.Scale(root, from_=6, to=32,
                         orient="horizontal", length=260,
                         bg="#f0f0f0", highlightthickness=0)
length_slider.set(16)
length_slider.pack()


options_frame = tk.Frame(root, bg="#f0f0f0")
options_frame.pack(pady=8)

var_upper   = tk.BooleanVar(value=True)
var_lower   = tk.BooleanVar(value=True)
var_digits  = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=False)

tk.Checkbutton(options_frame, text="Majuscule (A-Z)", variable=var_upper,
               bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Minuscule (a-z)", variable=var_lower,
               bg="#f0f0f0").grid(row=0, column=1, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Cifre (0-9)",     variable=var_digits,
               bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Simboluri (!@#)", variable=var_special,
               bg="#f0f0f0").grid(row=1, column=1, sticky="w", padx=10)


tk.Button(root, text="Genereaza",
          font=("Helvetica", 10, "bold"),
          bg="#4a90d9", fg="white",
          relief="flat", padx=20, pady=6,
          cursor="hand2",
          command=generate_password).pack(pady=(10, 6))


result_frame = tk.Frame(root, bg="#f0f0f0")
result_frame.pack()

result_var = tk.StringVar(value="")
tk.Entry(result_frame, textvariable=result_var,
         font=("Courier", 11), width=24,
         state="readonly", readonlybackground="white",
         relief="solid", bd=1).pack(side="left", padx=(0, 6))

copy_btn = tk.Button(result_frame, text="Copiaza",
                     font=("Helvetica", 9),
                     relief="flat", bg="#e0e0e0",
                     padx=8, pady=4,
                     cursor="hand2",
                     command=copy_password)
copy_btn.pack(side="left")

root.mainloop()
