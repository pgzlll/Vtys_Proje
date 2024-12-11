import tkinter as tk
from tkinter import messagebox
import mysql.connector
from task_add import add_task
from db_connection import db


# Veritabanı bağlantısı
db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="CaPut149DraCoNi5", 
    database="project_management"
)

# Tkinter ana pencere
root = tk.Tk()
root.title("Proje Yönetim Sistemi")
root.geometry("600x400")

# Tüm projeleri görüntüleme
def view_projects():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()

    result_window = tk.Toplevel(root)
    result_window.title("Projeler")
    
    tk.Label(result_window, text="Projeler", font=("Arial", 16)).pack()
    
    for project in projects:
        project_info = f"ID: {project[0]}, Adı: {project[1]}, Başlangıç: {project[2]}, Bitiş: {project[3]}"
        tk.Label(result_window, text=project_info).pack()

# Yeni proje ekleme
def add_project():
    def save_project():
        name = name_entry.get()
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()

        cursor = db.cursor()
        cursor.execute("INSERT INTO projects (project_name, start_date, end_date) VALUES (%s, %s, %s)", (name, start_date, end_date))
        db.commit()
        messagebox.showinfo("Başarılı", "Proje eklendi!")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Yeni Proje Ekle")

    tk.Label(add_window, text="Proje Adı:").pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    tk.Label(add_window, text="Başlangıç Tarihi (YYYY-MM-DD):").pack()
    start_date_entry = tk.Entry(add_window)
    start_date_entry.pack()

    tk.Label(add_window, text="Bitiş Tarihi (YYYY-MM-DD):").pack()
    end_date_entry = tk.Entry(add_window)
    end_date_entry.pack()

    tk.Button(add_window, text="Kaydet", command=save_project).pack()

# Proje silme
def delete_project():
    def confirm_delete():
        project_id = project_id_entry.get()

        cursor = db.cursor()
        cursor.execute("DELETE FROM projects WHERE project_id = %s", (project_id,))
        db.commit()

        messagebox.showinfo("Başarılı", f"Proje (ID: {project_id}) başarıyla silindi!")
        delete_window.destroy()

    delete_window = tk.Toplevel(root)
    delete_window.title("Proje Sil")

    tk.Label(delete_window, text="Silmek İstediğiniz Proje ID'sini Girin:").pack()
    project_id_entry = tk.Entry(delete_window)
    project_id_entry.pack()

    tk.Button(delete_window, text="Sil", command=confirm_delete).pack()

# Ana menü
tk.Label(root, text="Proje Yönetim Sistemi", font=("Arial", 20)).pack()

tk.Button(root, text="Projeleri Görüntüle", command=view_projects, width=30, height=2).pack(pady=10)
tk.Button(root, text="Yeni Proje Ekle", command=add_project, width=30, height=2).pack(pady=10)
tk.Button(root, text="Projeyi Sil", command=delete_project, width=30, height=2).pack(pady=10)
tk.Button(root, text="Yeni Görev Ekle", command=add_task, width=30, height=2).pack(pady=10)


root.mainloop()
