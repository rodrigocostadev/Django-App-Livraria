from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.utils import timezone
from .forms import SignUpForm, AddBookForm
from .models import Book

# Create your views here.
def home(request):
    # return HttpResponse('Teste Home')
    books = Book.objects.all()

    # Se eu fiz uma requisição do tipo post:
    if request.method == "POST":
        username = request.POST['usuario'] # Pega o usuario atraves do atributo name do input do html 
        password = request.POST['senha'] # Pega o usuario atraves do atributo name do input do html 
        
        user = authenticate(
            request,
            username = username,
            password = password
        )
        
        if user is not None:
            login(request,user)
            messages.success(request,'Login realizado com sucesso')
            return redirect('home')
        else:
            messages.error(request,"Erro na autenticação. Tente novamente!")
            return redirect('home')
        
    # Se eu não realizei nenhuma requisição e ja estou autenticado, vai para o else (vai para a home)
    else:
        return render(request, 'home.html',{'books':books})



def logout_user(request):
    logout(request)
    messages.success(request,"Você fez logout")
    return redirect('home')



# Função para cadastrar um novo usuario, após cadastrar o usuario ja é logado automaticamente
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST) # vai passar os dados da requisição via post para a variavel form
        if form.is_valid():
            form.save() # Registra o usuário no banco de dados, criando o novo usuário.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            # EXPLICAÇÃO DO METODO CLEANED_DATA:
            
            # Quando você chama form.is_valid(), o Django valida todos os campos do formulário e, caso estejam 
            # corretos, os armazena em um dicionário chamado cleaned_data.
            
            # Após a validação, form.cleaned_data contém os valores finais e seguros que o usuário forneceu. Então, as linhas:
                # username = form.cleaned_data['username']
                # password = form.cleaned_data['password1']
            # estão extraindo os valores validados para usá-los em outro contexto, como, neste caso, para autenticar o usuário.
            
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Você fez login com sucesso com o novo usuário!")
            return redirect('home')
        
    # O else é usado apenas para exibir o formulário vazio quando a página de registro é carregada pela primeira vez ou após um erro na validação do formulário.
    else:
        form = SignUpForm()
        return render (request,'register.html',{'form':form})
    return render (request,'register.html', {'form':form})




# Só vai acessar os detalhes do livro se estiver autenticado
def book_detail(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id =id)
        return render(request, 'book.html', {'book':book})  # {'book': book} é um dicionário sendo passado para o contexto da página que será renderizada.
    else:
        messages.error(request, 'Você precisa estar logado!')
        return redirect('home')


# Só vai deletar o livro se estiver autenticado
def book_delete(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id = id)
        book.delete()
        messages.success(request, "Livro excluído com sucesso!")
        return redirect('home')
    else:
        messages.error(request,'Voce precisa estar logado!')
        return redirect('home')


def book_add(request):
    form = AddBookForm(request.POST or None, request.FILES or None ) # Se não tiver nenhuma requisição o valor de form vai ser none
    if request.user.is_authenticated: # Se o usuario estiver autenticado
        if request.method == "POST": # se o metodo da requisição for igual a post
            if form.is_valid(): # se todos os dados do formulário forem validos
                form.save() # salva o formulário
                messages.success(request, "Livro adicionado com sucesso")
                return redirect('home') # redireciona para a home            
        return render(request, 'add_book.html', {'form':form})
    
    # EXPLICAÇÃO:
    # render(request, 'add_book.html'): Acontece quando:
    #     O usuário está autenticado e a requisição é GET (primeira vez que acessa a página).
    #     O formulário ainda não foi enviado.
    # redirect('home'): Acontece quando:
    #     O usuário está autenticado e o formulário foi enviado e validado (requisão POST).
    #     O usuário não está autenticado, e uma tentativa de adicionar o livro é feita (isso ocorre imediatamente após a verificação de autenticação). 
    #     O código redireciona o usuário para a página inicial (home).
        
    else: # Se o usuário não estiver autenticado
        messages.error(request, 'Voce deve estar autenticado para adicionar livro!')
        return redirect('home')
    
    
    
    
    
def book_update(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        # print(book)
        book.last_update = timezone.now()
        form = AddBookForm(request.POST or None, instance=book) # (request.POST or None) Se não tiver nenhuma requisição o valor de form vai ser none
        # (Instance=book)  o formulário será pré-preenchido com os dados do livro clicado/escolhido
        
        if form.is_valid():
            form.save()
            messages.success(request, "Livro atualizado com sucesso!")
            return redirect('home')
        
        return render(request,'update_book.html', {'form':form})
    else:
        messages.error(request, 'Voce deve estar autenticado para atualizar o livro!')
        
        
        
        
        
        
        
        
        
        
        

# def sobre(request):
#     return HttpResponse("Teste Sobre")
    
    
    
    
    
    
    
    
    
    