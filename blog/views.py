from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
# Le point avant models signifie dossier courant 
# Les fichiers views.py et models.py sont dans le même répertoire. Cela signifie que nous pouvons utiliser . + nom du fichier (sans .py). 
# Ensuite, nous importons le modèle (Post).
from .forms import PostForm
# Afin de pouvoir créer un nouveau formulaire Post, nous avons besoin d'appeler la fonction PostForm() et de la passer au template

# VOIR LA LISTE DES POSTS
# création d'une vue "post_list" auquelle blog/urls.py fait référence
# on créé une fonction (def) appelée post_list qui prend une request et qui va return la valeur donnée par une autre fonction render qui va assembler notre template blog/post_list.html.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    # Dans la fonction render, nous avons un paramètre request, qui désigne tout ce que nous recevons d'un utilisateur par l'intermédiaire d'Internet, et un autre qui signale le fichier template ('blog/post_list.html'). Le dernier paramètre, {}, va nous permettre de glisser des informations que notre template va utiliser. Nous devons donner des noms à ces informations (nous allons rester sur 'posts' pour le moment). :) Ça va ressembler à ça : {'posts': posts}. La partie située avant : est une chaine de caractères ; vous devez donc l'entourer de guillemets : ''

# VOIR EN DETAILS LE POST
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# CREER UN POST
def post_new(request):
    # quand on revient à la vue avec les données que l'on a saisies dans le formulaire
    # Si method contient POST alors on veut construire le PostForm avec les données du formulaire
    if request.method == "POST":
        
        form = PostForm(request.POST)
        # si le formulaire a été rempli correctement, on le sauvegarde
        if form.is_valid():
            # nous n'enregistrons pas directement le formulaire
            post = form.save(commit=False)
            # nous ajoutons d'abord un auteur d'article qui est l'user connecté
            post.author = request.user
            # nous ajoutons la date et heure de publication qui sera égale à la date et heure actuelle
            post.published_date = timezone.now()
            # nous sauvegardons le post
            post.save()
            # on se redirige sur la vue post_detail du post qu'on vient de créer (une vue à besoin d'une variable pk)
            return redirect('post_detail', pk=post.pk)
    # la première quand on accède à la page pour la première fois et nous voulons un formulaire vide 
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# EDITER UN POST
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})