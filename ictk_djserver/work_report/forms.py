from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        # labels = {
        #     'title': 'Titulo',
        #     'publication_date': 'Data de Publicação',
        #     'author': 'Autor',
        #     'price': 'Preço',
        #     'pages': 'Número de Páginas',
        #     'book_type': 'Formato'
        # }
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'publication_date': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.TextInput(attrs={'class': 'form-control'}),
        #     'price': forms.TextInput(attrs={'class': 'form-control'}),
        #     'pages': forms.TextInput(attrs={'class': 'form-control'}),
        #     'book_type': forms.TextInput(attrs={'class': 'form-control'}),
        # }