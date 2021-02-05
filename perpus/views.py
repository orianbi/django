from django.shortcuts import redirect, render, reverse
from django.http import HttpResponseRedirect
from .forms import FormBuku
from .models import Buku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, User


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    title = "Belajar Django"
    judul = "Halaman Utama"

    konteks = {
        "title": title,
        "judul": judul,
    }
    return render(request, "index.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    title = "Belajar Django"
    judul = "Halaman Buku"
    bukus = Buku.objects.all()
    konteks = {"title": title, "judul": judul, "bukus": bukus}
    return render(request, "buku.html", konteks)


def penerbit(request):
    return HttpResponseRedirect("Halaman Penerbit")


@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form = FormBuku()
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect("buku")
        else:
            messages.warning(request, "Data Gagal Ditambahkan")
    else:
        form = FormBuku()
        title = "Belajar Django"
        judul = "Halaman Buku"

        konteks = {
            "title": title,
            "judul": judul,
            "form": form,
        }

    return render(request, "tambah-buku.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id):
    buku = Buku.objects.get(id=id)
    templates = "ubah_buku.html"
    if request.method == "POST":
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid:
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect("buku")

        else:
            messages.error(request, "Data Gagal Diubah")
    else:
        form = FormBuku(instance=buku)

        konteks = {
            "form": form,
            "buku": buku,
        }
    return render(request, templates, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus(request, id):
    buku = Buku.objects.get(id=id)
    buku.delete()
    messages.error(request, "Data Berhasil Dihapus")
    return HttpResponseRedirect(reverse("buku"))


def signup(request):
    title = "Belajar Djanog"
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Dibuat")
            return redirect("user")
        else:
            messages.error(request, "User Gagal Dibuat")
            return redirect("signup")
    else:
        form = UserCreationForm()
        konteks = {
            "form": form,
            "title": title,
        }
    return render(request, "signup.html", konteks)


@login_required(login_url=settings.LOGIN_URL)
def user(request):
    title = "Belajar Djanog"
    judul = "Halaman User"
    users = User.objects.all()
    konteks = {
        "title": title,
        "judul": judul,
        "users": users,
    }
    return render(request, "user.html", konteks)


def hapusUser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.error(request, "User Berhasil Dihapus")
    return HttpResponseRedirect(reverse("user"))


def ubahUser(request, id):
    user = User.objects.get(id=id)
    templates = "ubah_user.html"
    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "User Berhasil Diubah")
            return redirect("user")
    else:
        form = User()

        konteks = {
            "form": form,
            "user": user,
            "templates": templates,
        }
    return render(request, templates, konteks)
