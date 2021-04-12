import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
def err():
    tk.messagebox.showinfo(title='hello', message='hello')

info = tk.Label(root, text="Halo ini adalah GUI sederhana menggunakan python")
info.pack()

erro = tk.Button(root, text="Top", command=err)
erro.pack()

root.mainloop()