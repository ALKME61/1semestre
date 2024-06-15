# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    # Функция-обработчик для кнопки Submit
    result = messagebox.showinfo("Submitted", "Form Submitted")
    print(result)

root = tk.Tk()
root.title("All Fields Form")
root.geometry("450x800")
root.resizable(False, False)

# Заголовок формы
title_label = tk.Label(root, text="ALL FIELDS FORM", font=("Helvetica", 16, "bold"), fg="blue")
title_label.pack(pady=10)

# Textfield
tk.Label(root, text="Textfield").pack(anchor='w')
textfield = tk.Entry(root, width=50)
textfield.pack(pady=5)

# Textarea
tk.Label(root, text="Textarea").pack(anchor='w')
textarea = tk.Text(root, width=50, height=5)
textarea.pack(pady=5)

# Email address
tk.Label(root, text="Email Address").pack(anchor='w')
email_field = tk.Entry(root, width=50)
email_field.pack(pady=5)

# Dropdown
tk.Label(root, text="Dropdown").pack(anchor='w')
options = ["Option 1", "Option 2", "Option 3"]
dropdown = ttk.Combobox(root, values=options)
dropdown.set(options[0])
dropdown.pack(pady=5)

# Radio Button
tk.Label(root, text="Radio Button").pack(anchor='w')
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio1.pack(anchor='w')
radio2.pack(anchor='w')

# Checkbox
tk.Label(root, text="Checkbox").pack(anchor='w')
check1 = tk.Checkbutton(root, text="Option 1")
check2 = tk.Checkbutton(root, text="Option 2")
check3 = tk.Checkbutton(root, text="Option 3")
check1.pack(anchor='w')
check2.pack(anchor='w')
check3.pack(anchor='w')

# Password
tk.Label(root, text="Password").pack(anchor='w')
password_field = tk.Entry(root, show='*', width=50, bg='#ffffe0')
password_field.pack(pady=5)

# Number Field
tk.Label(root, text="Number Field").pack(anchor='w')
number_field = tk.Entry(root, width=50)
number_field.pack(pady=5)

# Mathematical Captcha
tk.Label(root, text="Mathematical Captcha").pack(anchor='w')
captcha_frame = tk.Frame(root)
captcha_frame.pack(anchor='w')
captcha_label = tk.Label(captcha_frame, text="6 + 8 =")
captcha_label.pack(side='left')
captcha_entry = tk.Entry(captcha_frame, width=10)
captcha_entry.pack(pady=5, side='left')

# Google Captcha (not functional, just for demo)
tk.Label(root, text="Google Captcha").pack(anchor='w')
captcha_check = tk.Checkbutton(root, text="I'm not a robot")
captcha_check.pack(anchor='w', pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

root.mainloop()
