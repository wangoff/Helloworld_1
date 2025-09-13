import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Привет, {name}!")

root = tk.Tk()
root.title("Приветствие")
root.geometry("300x200")

label = tk.Label(root, text="Введите ваше имя:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Поздороваться", command=greet)
button.pack(pady=10)

# играемся с цветами
label.config(fg="blue", font=("Arial", 14))
root.config(bg="lightyellow")


root.mainloop()