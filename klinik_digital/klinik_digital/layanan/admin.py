from django.contrib import admin
# Kita panggil model yang tadi dibuat
from .models import Dokter, Pasien, Pendaftaran

# Kita suruh Django nampilin tabel ini di halaman Admin
admin.site.register(Dokter)
admin.site.register(Pasien)
admin.site.register(Pendaftaran)