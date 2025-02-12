from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book, Comment, RatinStar
import datetime


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '''
        <span class=" form-text text-muted " >
            <small>Obrigatório. 150 caracteres ou menos. Letras, digitos e alguns caracteres</small>
        </span> 
        '''
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''
        <ul class=" form-text text-muted small" >
            <li>Senha deve ser única.</li>
            <li>Senha deve conter pelo menos 8 caracteres.</li>
            <li>Senha deve ser totalmente numérica.</li>
        </ul> 
        '''
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '''
        <span class=" form-text text-muted " >
            <small>Digite a mesma senha digitada no campo anterior.</small>
        </span> 
        '''



class AddBookForm(forms.ModelForm):
    genre_choices = [
        ('','Selecione o Gênero'),
        ('Auto Ajuda', 'Auto ajuda'),
        ('Biografia', 'Biografia'),
        ('Desenvolvimento Pessoal', 'Desenvolvimento Pessoal'),
        ('Empreendedorismo', 'Empreendedorismo'),
        ('Estratégia', 'Estratégia'),
        ('Ficção', 'Ficção'),
        ('Finanças', 'Finanças'),
        ('Gestao/Lideranca', 'Gestão e Liderança'),
        ('Tecnologia', 'Tecnologia'),
    ]
    
    # current_year = datetime.datetime.now().year # Pega o ano atual a partir da biblioteca datetime
    # year_choices = [('','Escolha o ano')]
    # for year in range(current_year,1799, -1): # -1 é o passo negativo que faz com que a sequencia seja gerada de forma decrescente
    #     year_choices.append((year,year))        
    
    title = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Título Livro","class":"form-control"}), label = "")
    description = forms.CharField(required=True, widget = forms.widgets.Textarea(attrs={"placeholder":"Descrição Livro","class":"form-control"}), label = "")
    year = forms.CharField(required=True, label="")
    # year = forms.IntegerField(required=True, label="")
    # year = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Ano Livro","class":"form-control", "list":"year_choices"}), label = "")
    # year = forms.ChoiceField(choices=year_choices,required=True, widget = forms.widgets.Select(attrs={"placeholder":"Ano Livro","class":"form-control"}), label = "")
    # year = forms.IntegerField(required=True, widget = forms.widgets.NumberInput(attrs={"placeholder":"Ano Livro","class":"form-control"}), label = "")
    # genre = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Gênero Livro","class":"form-control"}), label = "")
    genre = forms.ChoiceField(choices = genre_choices, required=True, widget = forms.widgets.Select(attrs={"placeholder":"Gênero Livro","class":"form-control"}), label = "")
    value = forms.IntegerField(required=True, widget = forms.widgets.NumberInput(attrs={"placeholder":"Valor Livro","class":"form-control"}), label = "")
    stock = forms.IntegerField(required=True, widget = forms.widgets.NumberInput(attrs={"placeholder":"Estoque","class":"form-control"}), label="")
    image = forms.ImageField(widget = forms.widgets.FileInput(attrs={"class":"form-control"}), label = "Imagem")
    # comments = forms.CharField(required=False, widget = forms.widgets.Textarea(attrs={"placeholder":"Adicione um comentário","class":"form-control"}), label = "", initial="")
    
    class Meta:
        model = Book
        fields = ('title', 'description', 'year', 'genre', 'value','stock','image')
        
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
    
    # Campos preenchidos automaticamente:
    book = forms.ModelChoiceField(queryset=Book.objects.all(),widget=forms.HiddenInput(), required=False)
    user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput(), required=False)

    # Campo de comentário preenchido pelo usuário:
    text = forms.CharField(
        required=True, 
        widget = forms.Textarea(attrs={"placeholder":"Adicione um comentário. (Limite de 300 caracteres)","class":"form-control"}), 
        label = "", 
        max_length=300) # Limita o numero de caracteres a serem digitados.



class RatingForm(forms.ModelForm):
    class Meta:
        model = RatinStar
        fields = ['rating']
        
    # Campos preenchidos automaticamente:
    book = forms.ModelChoiceField(queryset=Book.objects.all(),widget=forms.HiddenInput(), required=False)
    user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput(), required=False)
    
    # Campo de avaliação "Estrelas" preenchido pelo usuário:
    rating = forms.DecimalField(required=True,min_value=1,max_value=5,widget=forms.RadioSelect(choices=[(i,str(i)) for i in range(1,6)]))








