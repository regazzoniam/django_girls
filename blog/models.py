from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # models.Model signifie qu'il s'agit d'un modele Django
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # lien vers un autre modèle
    title = models.CharField(max_length=200)
    # définition d'un champ texte avec nombre de caractères limité
    text = models.TextField()
    # définition d'un champ texte avec nombre de caractères ilimité
    created_date = models.DateTimeField(default=timezone.now)
    # le champ est un horodatage (date et heure)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # méthode publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title