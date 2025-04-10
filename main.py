import customtkinter
from CTkToolTip import *
import random
import string
import clipboard

def show_value(value):
    tooltip_1.configure(message=int(value))

def generate():
    digits = digits_check.get()
    lower = lower_check.get()
    upper = upper_check.get()
    di = string.digits
    up = string.ascii_uppercase
    low = string.ascii_lowercase
    quant = int(slider.get())
    if not digits and not lower and not upper:
        window = customtkinter.CTkToplevel()
        window.title('атата')
        window.grab_set()
        window.geometry(f'240x120+{width // 2 - 120}+{height // 2 - 60}')
        message = customtkinter.CTkLabel(
            master=window,
            text='нужно выбрать параметры пароля',
            text_color='#405CE0'
            )
        message.place(x = 120, y = 60, anchor = 'center')
        return
    elif digits and not lower and not upper:
        password = ''.join([random.choice(di) for _ in range(quant)])
    elif digits and lower and not upper:
        password = ''.join([random.choice(di+low) for _ in range(quant)])
    elif digits and not lower and upper:
        password = ''.join([random.choice(di + up) for _ in range(quant)])
    elif not digits and lower and not upper:
        password = ''.join([random.choice(low) for _ in range(quant)])
    elif not digits and lower and upper:
        password = ''.join([random.choice(up+low) for _ in range(quant)])
    elif not digits and not lower and upper:
        password = ''.join([random.choice(up) for _ in range(quant)])
    elif digits and lower and upper:
        password = ''.join([random.choice(di+low+up) for _ in range(quant)])

    psw.configure(text=password)

app = customtkinter.CTk()
app.title('password')
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f'480x360+{width//2 - 240}+{height//2 - 180}')
app.minsize(480, 360)
app.maxsize(600, 480)
app.grid_rowconfigure(tuple(range(8)), weight=1)
app.grid_columnconfigure(tuple(range(6)), weight=1)
text = customtkinter.CTkLabel(
    master=app,
    text='не нажимай эту кнопку',
    text_color='#405CE0'
)
text.grid(row=0, column=0, sticky='nsew', columnspan=6)

digits_check = customtkinter.CTkCheckBox(app, text='цифры', text_color='#405CE0')
digits_check.grid(row=1, column=1, sticky='nw')

upper_check = customtkinter.CTkCheckBox(app, text='верхний регистр', text_color='#405CE0')
upper_check.grid(row=2, column=1, sticky='nw')

lower_check = customtkinter.CTkCheckBox(app, text='нижний регистр', text_color='#405CE0')
lower_check.grid(row=3, column=1, sticky='nw')

slider = customtkinter.CTkSlider(app, from_=4, to=16, command=show_value)
slider.grid(row=4, column=0, columnspan=6)
tooltip_1 = CTkToolTip(slider, message="10")

button = customtkinter.CTkButton(app,
                                 text='кнопка',
                                 fg_color='#405CE0',
                                 text_color='#FFFFFF',
                                 command= generate)

button.grid(row=5, column=0, columnspan=6)

copy_button = customtkinter.CTkButton(app,
                                 text='скопировать',
                                 fg_color='#405CE0',
                                 text_color='#FFFFFF',
                                 command=lambda: clipboard.copy(psw.cget('text'))
                                 )

copy_button.grid(row=6, column=0, columnspan=6)

psw = customtkinter.CTkLabel(
    master=app,
    text='password',
    text_color='#405CE0'
)
psw.grid(row=7, column=0, sticky='nsew', columnspan=6)

app.mainloop()