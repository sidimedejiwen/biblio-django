from django.shortcuts import render
from .models import Livre

def liste_livres(request):
    q = request.GET.get("q", "")
    livres = Livre.objects.all().order_by("titre")
    if q:
        livres = livres.filter(titre__icontains=q) | livres.filter(auteur__icontains=q)
    return render(request, "livres/liste.html", {"livres": livres, "q": q})