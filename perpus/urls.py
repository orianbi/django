from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from website import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("buku/", views.buku, name="buku"),
    path("penerbit/", views.penerbit, name="penerbit"),
    path("tambah-buku/", views.tambah_buku, name="tambah-buku"),
    path("hapus/<int:id>", views.hapus, name="hapus"),
    path("ubah_buku/<int:id>", views.ubah_buku, name="ubah_buku"),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("user/", views.user, name="user"),
    path("ubah_user/<int:id>", views.ubahUser, name="ubah_user"),
    path("hapus_user/<int:id>", views.hapusUser, name="hapus_user"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
