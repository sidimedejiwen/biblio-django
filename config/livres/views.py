from django.shortcuts import render
from .models import Livre

def liste_livres(request):
    livres = Livre.objects.all().order_by("titre")
    return render(request, "livres/liste.html", {"livres": livres})