from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Nous enregistrons notre modèle pour qu'il soit visible dans l'interface d'administration
