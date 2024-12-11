<<<<<<< HEAD
# Proje Yönetim Sistemi (Tkinter)

Bu proje, Python ve Tkinter kullanarak masaüstü bir Proje Yönetim Sistemi oluşturmayı sağlar. Uygulama, projeleri, görevleri ve çalışanları yönetmek için kullanıcı dostu bir arayüz sunar.

## Özellikler
- Proje oluşturma, listeleme, güncelleme ve silme.
- Görev oluşturma, görüntüleme ve durum güncelleme.
- Çalışan ekleme ve görev atama.

## Gerekli Yazılımlar
- Python (3.8 veya üstü)
- MySQL Server

## Kurulum Adımları

### 1. **Veritabanı Ayarları**
1. MySQL kurulumunu tamamlayın ve başlatın.
2. Komut satırında MySQL'e bağlanarak aşağıdaki SQL komutlarını çalıştırın:
   ```sql
   CREATE DATABASE project_management;

   USE project_management;

   CREATE TABLE projects (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       start_date DATE NOT NULL,
       end_date DATE NOT NULL
   );

   CREATE TABLE employees (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       tasks_completed_on_time INT DEFAULT 0,
       tasks_not_completed_on_time INT DEFAULT 0
   );

   CREATE TABLE tasks (
       id INT AUTO_INCREMENT PRIMARY KEY,
       project_id INT NOT NULL,
       employee_id INT DEFAULT NULL,
       name VARCHAR(255) NOT NULL,
       start_date DATE NOT NULL,
       end_date DATE NOT NULL,
       man_day INT NOT NULL,
       status ENUM('BAŞLAYACAK', 'TAMAMLANDI', 'DEVAM EDİYOR') DEFAULT 'BAŞLAYACAK',
       FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
       FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE SET NULL
   );
=======
# Vtys_Proje
>>>>>>> f16659b4ad8bfd31ff94168a5bb398961dd23920
