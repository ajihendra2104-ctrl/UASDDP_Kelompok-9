from django.shortcuts import render, redirect, get_object_or_404 # <--- Tambah redirect & get_object
from .models import Dokter
from .forms import FormPendaftaran # <--- BARU: Import form yang tadi dibuat

def halaman_dokter(request):
    # 1. Ambil semua data dokter dari database
    semua_dokter = Dokter.objects.all()
    
    # 2. Bungkus data biar bisa dibawa ke HTML
    context = {
        'dokter_list': semua_dokter
    }
    
    # 3. Kirim ke file HTML (nanti kita buat file ini)
    return render(request, 'daftar_dokter.html', context)

def daftar_berobat(request, id_dokter):
    # 1. Cari dokter berdasarkan ID yang diklik
    dokter_tujuan = get_object_or_404(Dokter, id=id_dokter)

    # 2. Jika tombol 'Simpan' diklik (POST)
    if request.method == 'POST':
        form = FormPendaftaran(request.POST)
        if form.is_valid():
            data_pendaftaran = form.save(commit=False)
            data_pendaftaran.dokter = dokter_tujuan # Set dokternya otomatis
            data_pendaftaran.save() # Simpan ke database
            return redirect('index') # Balik ke halaman utama

    # 3. Jika baru buka halaman (GET)
    else:
        form = FormPendaftaran()

    context = {
        'form': form,
        'dokter': dokter_tujuan
    }
    return render(request, 'form_pendaftaran.html', context)