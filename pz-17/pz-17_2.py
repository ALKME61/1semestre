# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9. Я взял из второй
# Дано расстояние L в сантиметрах. Используя операцию деления
# нацело, найти количество полных метров в нем (1 метр =100 см).

import tkinter as tk

def convert_cm_to_meters():
    """Функция для конвертации сантиметров в метры"""
    try:
        cm = int(cm_entry.get())
        meters = cm / 100
        result_label.config(text=f"Результат в метрах: {meters}")
    except ValueError:
        result_label.config(text="Введите число!")

# Создание окна
window = tk.Tk()
window.title("Конвертер сантиметров в метры")
window.geometry("400x200")
window.resizable(False, False)

# Надпись для ввода
cm_label = tk.Label(window, text="Введите расстояние в см:")
cm_label.pack()

# Поле ввода
cm_entry = tk.Entry(window)
cm_entry.pack()

# Кнопка конвертации
convert_button = tk.Button(window, text="Конвертировать", command=convert_cm_to_meters)
convert_button.pack()

# Метка для вывода результата
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()