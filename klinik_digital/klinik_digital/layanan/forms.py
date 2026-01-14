from django import forms
from .models import Pendaftaran

class FormPendaftaran(forms.ModelForm):
    class Meta:
        model = Pendaftaran
        # Kita cuma butuh input Pasien dan Keluhan
        # (Dokter nanti otomatis dipilih sistem, Tanggal otomatis hari ini)
        fields = ['pasien', 'keluhan']
        
        # Ini buat nambahin class Bootstrap ke inputannya biar cantik
        widgets = {
            'pasien': forms.Select(attrs={'class': 'form-select'}),
            'keluhan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }