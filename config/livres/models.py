from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    annee = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titre} - {self.auteur}"