from django.db import models

# 1. Tabel Dokter
class Dokter(models.Model):
    nama = models.CharField(max_length=100)
    spesialisasi = models.CharField(max_length=100) # Contoh: Gigi, Umum
    no_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

# 2. Tabel Pasien
class Pasien(models.Model):
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()

    def __str__(self):
        return self.nama

# 3. Tabel Pendaftaran (Hubungin Dokter & Pasien)
class Pendaftaran(models.Model):
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    dokter = models.ForeignKey(Dokter, on_delete=models.CASCADE)
    tanggal_daftar = models.DateTimeField(auto_now_add=True)
    keluhan = models.TextField()

    def __str__(self):
        return f"{self.pasien.nama} - {self.dokter.nama}"