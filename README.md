# capstoneproject
Capstone Project Kelompok 3 kelas Stego (Intelligence Cloud Track)

# Capstone Project Kelompok 3 Stego 2022
1. Luthfi Fachruddin
2. Khairunnisa
3. Muhammad Ariyadi
4. Keyrien Liana
5. Jesita Dosma

# Face_Recognition_Attendance
Presensi menggunakan Azure SQL Database dan Python

Mengambil absensi melalui kamera dengan menganalisis gambar yang disimpan dan membandingkannya dengan gambar kamera menggunakan pengenalan wajah dan disimpan dalam layanan database Azure sql.


# Cara Instalasi

Install terlebih dahulu library yang dibutuhkan:
1. cv2 >> pip install opencv-python
2. numpy>> pip install numpy
3. face_recognition >> tutorial: https://www.geeksforgeeks.org/how-to-install-face-recognition-in-python-on-windows/
4. pyodbc>> pip install pyodbc

ODBC Driver >> https://www.microsoft.com/en-us/download/details.aspx?id=56567

Lalu
Create the Azure Sql database cognitive service resource on Azure portal (https://portal.azure.com/)


Untuk Syntax Query Hapus Table
DROP TABLE [dbo].[StudentAttendance]

Untuk Syntax Query Melihat data dari Tabel
SELECT TOP (1000) * FROM [dbo].[StudentAttendance]


