import tkinter as tk
from tkinter import messagebox

def show_error():
    while True:
        messagebox.showerror("Ошибка системы", "Обнаружен вирус! Удаление System32... (Шутка)")

# Запускаем (чтобы остановить, придется закрыть PyCharm или нажать стоп)
show_error()
