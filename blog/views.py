from django.shortcuts import render

# création d'une vue "post_list" auquelle blog/urls.py fait référence
# on créé une fonction (def) appelée post_list qui prend une request et qui va return la valeur donnée par une autre fonction render qui va assembler notre template blog/post_list.html.
def post_list(request):
    return render(request, 'blog/post_list.html', {})