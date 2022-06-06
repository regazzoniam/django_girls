from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Le point avant models signifie dossier courant 
# Les fichiers views.py et models.py sont dans le même répertoire. Cela signifie que nous pouvons utiliser . + nom du fichier (sans .py). 
# Ensuite, nous importons le modèle (Post).

# création d'une vue "post_list" auquelle blog/urls.py fait référence
# on créé une fonction (def) appelée post_list qui prend une request et qui va return la valeur donnée par une autre fonction render qui va assembler notre template blog/post_list.html.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    # Dans la fonction render, nous avons un paramètre request, qui désigne tout ce que nous recevons d'un utilisateur par l'intermédiaire d'Internet, et un autre qui signale le fichier template ('blog/post_list.html'). Le dernier paramètre, {}, va nous permettre de glisser des informations que notre template va utiliser. Nous devons donner des noms à ces informations (nous allons rester sur 'posts' pour le moment). :) Ça va ressembler à ça : {'posts': posts}. La partie située avant : est une chaine de caractères ; vous devez donc l'entourer de guillemets : ''

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})