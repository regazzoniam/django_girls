from django import forms
from .models import Post

# PostForm : nom du formulaire. On indique à Django que ce formulaire est un ModelForm : forms.ModelForm
class PostForm(forms.ModelForm):
    # La class Meta nous permet de dire à Django quel modèle il doit utiliser pour créer ce formulaire (model = Post)
    class Meta:
        # modele utilisé
        model = Post
        # champs qui vont apparaitre (ici titre et texte)
        fields = ('title', 'text',)