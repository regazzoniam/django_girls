from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # post/ : l’URL doit commencer par "post" suivi d’un /
    # <int:pk> : Django s’attend à une valeur entière (int), qu'en suite il transférera à une vue comme variable nommée "pk".
    # / : il nous faut un / à nouveau avant la fin de l’URL.
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]