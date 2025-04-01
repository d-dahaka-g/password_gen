import customtkinter
from CTkToolTip import *

def show_value(value):
    tooltip_1.configure(message=int(value))



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
                                 )

button.grid(row=5, column=0, columnspan=6)



app.mainloop()
