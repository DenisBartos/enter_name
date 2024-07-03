import customtkinter as ctk

ctk.set_appearance_mode('dark')

ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.geometry('400x400')
app.title("")


def login():
    new_window = ctk.CTkToplevel(app)

    new_window.title('New Window')

    new_window.geometry('50x50')


label = ctk.CTkLabel(app,text="")

label.pack(pady=20)


frame = ctk.CTkFrame(master=app)
frame.pack(pady=10,padx=10,fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text="Воход в систему управление коляской айтрекером")
label.pack(pady=12,padx=10)


user_entry= ctk.CTkEntry(master=frame,placeholder_text="Имя пользователя")
user_entry.pack(pady=5,padx=40)


button = ctk.CTkButton(master=frame,text="Входа",command=login)
button.pack(pady=26,padx=9)


def connect_to_tobii(driver_name):
    '''
    Это функция подключения привязки программы (имя) конкретно к драйверу тобби
    '''

    pass


def go_to_program_button():
    '''
    Это функция кнопки перейти к программе
    '''

    pass


app.mainloop()
