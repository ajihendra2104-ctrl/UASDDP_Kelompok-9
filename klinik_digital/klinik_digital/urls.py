from django.contrib import admin
from django.urls import path
from layanan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.halaman_dokter, name='index'), # Halaman Depan
    
    # URL Baru buat daftar (Perhatikan bagian <int:id_dokter>)
    path('daftar/<int:id_dokter>/', views.daftar_berobat, name='menu_daftar'),
]