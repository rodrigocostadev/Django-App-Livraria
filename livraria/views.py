from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
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
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            # EXPLICAÇÃO DO METODO CLEANED_DATA:
            
            # O cleaned_data contém um dicionário com os valores dos campos do formulário após a validação e a limpeza. 
            # Esses dados podem ser usados para acessar valores de forma segura e confiável.
            
            # form.cleaned_data['username']: Depois que o Django valida o campo username (verificando, por exemplo, se ele não está vazio, se não contém 
            # caracteres inválidos, etc.), o valor desse campo é armazenado em cleaned_data para uso posterior. 
            # Essa abordagem garante que os dados estejam corretos e seguros para uso.

            # form.cleaned_data['password1']: O campo password1 (a primeira senha inserida) também passa por um processo de validação 
            # (por exemplo, para verificar a força da senha, se ela tem pelo menos 8 caracteres, etc.), e o valor final e validado 
            # fica disponível em cleaned_data.

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Você fez login com sucesso com o novo usuário!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render (request,'register.html',{'form':form})
    return render (request,'register.html', {'form':form})

# def sobre(request):
#     return HttpResponse("Teste Sobre")


# Só vai acessar os detalhes do livro se estiver autenticado
def book_detail(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id =id)
        return render(request, 'book.html', {'book':book})
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
    form = AddBookForm(request.POST or None) # Se não tiver nenhuma requisição o valor de form vai ser none
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
        form = AddBookForm(request.POST or None, instance=book) # (request.POST or None) Se não tiver nenhuma requisição o valor de form vai ser none
        # (Instance=book)  o formulário será pré-preenchido com os dados do livro clicado/escolhido
        
        if form.is_valid():
            form.save()
            messages.success(request, "Livro atualizado com sucesso!")
            return redirect('home')
        
        return render(request,'update_book.html', {'form':form})
    else:
        messages.error(request, 'Voce deve estar autenticado para atualizar o livro!')
    
    
    
    
    
    
    
    
    
    