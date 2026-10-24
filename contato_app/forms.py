from django import forms


class FormularioContato(forms.Form):
    nome = forms.CharField(label='Nome:', required=True,max_length=100)

    email = forms.EmailField(
    label='Email:',
    required=True,
    max_length=100
)

    conteudo = forms.CharField(label='Conteudo:',widget=forms.Textarea)

   