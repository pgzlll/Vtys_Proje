import tkinter as tk
from tkinter import messagebox
import mysql.connector
from db_connection import db


def add_task():
    def save_task():
        project_id = project_id_entry.get()
        name = task_name_entry.get()
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        man_day = man_day_entry.get()

        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks (project_id, name, start_date, end_date, man_day) VALUES (%s, %s, %s, %s, %s)", 
                       (project_id, name, start_date, end_date, man_day))
        db.commit()
        messagebox.showinfo("Başarılı", "Görev eklendi!")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Yeni Görev Ekle")

    tk.Label(add_window, text="Proje ID:").pack()
    project_id_entry = tk.Entry(add_window)
    project_id_entry.pack()

    tk.Label(add_window, text="Görev Adı:").pack()
    task_name_entry = tk.Entry(add_window)
    task_name_entry.pack()

    tk.Label(add_window, text="Başlangıç Tarihi (YYYY-MM-DD):").pack()
    start_date_entry = tk.Entry(add_window)
    start_date_entry.pack()

    tk.Label(add_window, text="Bitiş Tarihi (YYYY-MM-DD):").pack()
    end_date_entry = tk.Entry(add_window)
    end_date_entry.pack()

    tk.Label(add_window, text="Man Day:").pack()
    man_day_entry = tk.Entry(add_window)
    man_day_entry.pack()

    tk.Button(add_window, text="Kaydet", command=save_task).pack()
    
