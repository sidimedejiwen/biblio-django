from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Emprunt(models.Model):
    livre = models.ForeignKey("livres.Livre", on_delete=models.CASCADE)
    lecteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_emprunt = models.DateField(default=timezone.now)
    date_retour = models.DateField(null=True, blank=True)
    def est_en_retard(self):
        return self.date_retour is None and \
            (timezone.now().date() - self.date_emprunt).days > 14