import tkinter as tk

from tkinter import messagebox

def save_text():
    text = text_box.get("1.0", tk.END).strip()
    if text:
        with open('user_text.txt', 'w', encoding='utf-8') as file:
            file.write(text)
        messagebox.showinfo("Сохранение", "Текст успешно сохранён!")
    else:
        messagebox.showwarning("Пустой ввод", "Нечего сохранять.")

def load_text():
    try:
        with open('user_text.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showwarning("Ошибка", "Файл не найден.")

root = tk.Tk()
root.title("Текстовый редактор")
root.geometry("400x300")

text_box = tk.Text(root, wrap=tk.WORD)
text_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

btn_save = tk.Button(root, text="Сохранить", command=save_text)
btn_save.pack(side=tk.LEFT, padx=10, pady=5)

btn_load = tk.Button(root, text="Загрузить", command=load_text)
btn_load.pack(side=tk.RIGHT, padx=10, pady=5)

root.mainloop()