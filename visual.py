# модуль visual.py будет отвечать за отрисовку gui, logic.py - за логику: высчитывание ответа

import logic  # подключаем наш модуль logic
import tkinter as tk  # подключаем модуль tkinter
import customtkinter as ctk  # подключаем модуль customtkinter

# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()  # создаём окно и привязываем его переменной root
root.title("Консольное приложение")  # устанавливаем заголовок окна
root.geometry("1500x900")  # устанавливаем размеры окна

# виджеты для окна 1
lbl_start_message = ctk.CTkLabel(master=root)
lbl_start_message.configure(text="Вопрос")
entry_input = ctk.CTkEntry(master=root)
entry_input.configure(justify="center")
btn_done = ctk.CTkButton(master=root)
btn_done.configure(text="Ответить")

# для позиционирования виджетов на экране используем сетку - grid
rows, columns = 3, 3
# пусть будет сетка 3 x 3, каждой строке и столбцу установим вес 1, чтобы сетка была равномерной
# индексы строк и столбцов начинаются с нуля
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

# # теперь расположим в ней наши виджеты
# # виджет можно расположить в одной ячейке, например, в ячейке (0, 2), тогда укажем row=0, column=2
# # а можно - в нескольких, например, в ячейках (0, 1) и (0, 2), тогда укажем: row=0, column=1, columnspan=2
# # то есть columnspan растягивает на 2 столбца

# отрисовываем окно 1
lbl_start_message.grid(row=0, column=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
entry_input.grid(row=1, column=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
btn_done.grid(row=2, column=1,ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")

root.mainloop()  # отображаем окно и запускаем цикл обработки событий окна для взаимодействия c пользователем