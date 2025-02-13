from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.utils import timezone
from .forms import SignUpForm, AddBookForm, CommentForm, RatingForm
from .models import Book, Comment, RatinStar, UserProfile



# Função para calcular a avaliação geral por estrelas
def calculate_media_rating(book):
    overall_rating = RatinStar.objects.filter(book=book) # pega as avaliações por livro (Query set)
    total_n_rating = 0 
    total_rating = 0 
    for item in overall_rating:
        total_rating += item.rating
        total_n_rating += item.n_review            
    # print(f"Esse é o total N rating {total_n_rating}")
    # print(f"Esse é o total rating {total_rating}")
    
    if overall_rating:
        media_rating = total_rating / total_n_rating
        media_rating = round(media_rating,1)
        # print(f"Esse é o media rating {media_rating}")
    else:
        media_rating = 0
    return media_rating



def home(request):
    # return HttpResponse('Teste Home')
    books = Book.objects.all().order_by('title') # Ordena em ordem alfabetica pelo titulo
    # book_id = Book.objects.get(id =id)
    # media_rating = calculate_media_rating(book_id)
    
    # for book in books:
    #     media_rating = calculate_media_rating(book)

    # Se eu fizer uma requisição do tipo post:
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
        form = SignUpForm(request.POST, request.FILES) # vai passar os dados da requisição via post para a variavel form
        if form.is_valid():
            
            # form.save() # Registra o usuário no banco de dados, criando o novo usuário.
            user = form.save()             # VER PORQUE NÃO FUNCIONA SEM O USER
            user_image = form.cleaned_data['user_image']
            cpf = form.cleaned_data['cpf']
            
            if user_image:
                user_profile = UserProfile.objects.create(user = user, user_image = user_image, cpf = cpf)
            else:
                user_profile = UserProfile.objects.create(user = user, cpf = cpf)
                
            user_profile.save()            
            
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
            
            if user is not None:
                login(request, user)
                messages.success(request, "Você fez login com sucesso com o novo usuário!")
                return redirect('home')
            else:
                messages.error(request, "Erro na autenticação. Tente novamente.")
                return redirect('register')
        
    # O else é usado apenas para exibir o formulário vazio quando a página de registro é carregada pela primeira vez ou após um erro na validação do formulário.
    else:
        form = SignUpForm()
        return render (request,'register.html',{'form':form})
    return render (request,'register.html', {'form':form})



# Só vai acessar os detalhes do livro se estiver autenticado
def book_detail(request, id):
    book = Book.objects.get(id =id)
    # user_image_profile = UserProfile.objects.get(id = id)
    
    if request.user.is_authenticated:        
        comment_form = CommentForm()  # Inicializando os formulários fora do bloco POST pra não dar erro nos comentarios e no ratingStar
        rating_form = RatingForm() # Inicializando os formulários fora do bloco POST pra não dar erro nos comentarios e no ratingStar
        
        # ///////////////////////////////////////////////////////////////////////////
        # AVALIAÇÃO GERAL DO LIVRO POR ESTRELAS:                
        media_rating = calculate_media_rating(book)
        
        if request.method == "POST":            
            
            # ///////////////////////////////////////////////////////////////////////////
            # DELETAR COMENTÁRIO:
            delete_comment_id = request.POST.get('delete_comment')
            if delete_comment_id:
                comment = get_object_or_404(Comment, id = delete_comment_id) # se o objeto não for encontrado, ele automaticamente gera um erro 404, sem você precisar lidar com a exceção manualmente.

                if request.user == comment.user or request.user.is_staff:
                    comment.delete()
                    messages.success(request, 'Comentário excluído com sucesso!')
                else:
                    messages.error(request,'Você não tem permissão para excluir o comentário!')            
            
            
            # ///////////////////////////////////////////////////////////////////////////
            # ADICIONAR COMENTÁRIO:
            if 'comment_submit' in request.POST: # Nome do botão de envio do formulário = 'comment_submit'
                comment_form = CommentForm(request.POST) # variavel comment_form recebe o valor do formulário de requisição
                if comment_form.is_valid():
                    
                    # ( comment = comment_form.save(commit=False) ) "Salva" o formulário sem enviar ao banco de dados "sem fazer o commit", 
                    # o que permite adicionar as  informações extras (como o livro e o usuário) para depois salvar e enviar ao banco de dados. 
                    # (Estou criando um objeto comment que recebe as informações do formulario, vou poder adicionar mais informações para salvar e enviar ao banco de dados )
                    comment = comment_form.save(commit=False) 
                    
                    comment.book = book
                    comment.user = request.user
                    comment.save()
                    
                    messages.success(request, 'Comentário adicionado com sucesso!')
                    return render(request, 'book.html', {'book':book})             
            
            
            # ///////////////////////////////////////////////////////////////////////////
            # ADICIONAR AVALIAÇÃO:
            if 'rating_submit' in request.POST: # Nome do botão de envio do formulário = 'rating_submit'                    
                
                rating_value = request.POST.get('rating') # Pega o valor do input através do name 'rating' do input
                rating_value = int(rating_value) # Passa para int pra comparar no if abaixo
                if rating_value and rating_value >= 1 and rating_value <= 5:
                    rating_form = RatingForm(request.POST) 
                    if rating_form.is_valid():
                        rating = rating_form.save(commit=False)
                        
                        rating.book = book
                        rating.user = request.user
                        rating.value = int(rating_value)
                        rating.n_review = 1               # SALVA o numero de avaliadores
                        rating.save()
                        media_rating = calculate_media_rating(book) # Atualiza a avaliação geral do livro ao enviar a nota de avaliação
                        # print(f"Esse é o media rating: {media_rating}")
                        # print(f"Antes de salvar: media_rating = {media_rating}, book.media_rating = {book.media_rating}")

                        book.media_rating = media_rating # Salva a media da avaliação geral do livro no modelo do livro
                        book.save()
                        print(f"Depois de salvar: media_rating = {media_rating}, book.media_rating = {book.media_rating}")
                        messages.success(request, 'Avaliação enviada com sucesso!')
                        return render(request, 'book.html', {'book':book, 'media_rating': media_rating}) 
                        # return redirect('book.html', id=book.id)                
   
        return render(request, 'book.html', {'book':book, 'comment_form':comment_form, 'rating_form': rating_form, 'media_rating': media_rating,})  # {'book': book} é um dicionário sendo passado para o contexto da página que será renderizada.
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
    
    # current_year = datetime.datetime.now().year # Pega o ano atual a partir da biblioteca datetime
    # year_choices = [('','Escolha o ano')]
    # for year in range(current_year,1799, -1): # -1 é o passo negativo que faz com que a sequencia seja gerada de forma decrescente
    #     year_choices.append((year,year))  
    
    # current_year = datetime.datetime.now().year # Pega o ano atual a partir da biblioteca datetime
    # # # year_choices = ['Escolha o ano']
    # year_choices = []
    # for year in range(current_year,1799, -1): # -1 é o passo negativo que faz com que a sequencia seja gerada de forma decrescente
    #     year_choices.append(str(year))    
    
    if request.user.is_authenticated: # Se o usuario estiver autenticado
        if request.method == "POST": # se o metodo da requisição for igual a post
            if form.is_valid(): # se todos os dados do formulário forem validos
                form.save() # salva o formulário
                messages.success(request, "Livro adicionado com sucesso")
                return redirect('home') # redireciona para a home            
        # return render(request, 'add_book.html', {'form':form, 'year_choices': year_choices,})
        return render(request, 'add_book.html', {'form':form,})
    
    # EXPLICAÇÃO:
    # render(request, 'add_book.html'): Acontece quando:
    #     O usuário está autenticado e a requisição é GET (primeira vez que acessa a página).
    #     O formulário ainda não foi enviado.
    # redirect('home'): Acontece quando:
    #     O usuário está autenticado e o formulário foi enviado e validado (requisão POST).
    #     O usuário não está autenticado, e uma tentativa de adicionar o livro é feita (isso ocorre imediatamente após a verificação de autenticação). 
    #     O código redireciona o usuário para a página inicial (home).
        
    else: # Se o usuário não estiver autenticado
        messages.error(request, 'Voce deve estar autenticado para adicionar o livro!')
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
        
        
        
def book_search(request):
    if request.user.is_authenticated:
        search_term = request.GET.get('search')
        
        if search_term:
            books = Book.objects.filter(title__icontains = search_term) # Filtra os livros pelo título
        else:
            return redirect('home')
            # books = Book.objects.all() # Se não houver termo de busca, mostra todos os livros
    
    else:
        # books = [] # quando o usuário não está autenticado (else: books = []) vai garantir que nenhum livro será mostrado na página de busca.
        return redirect('home')
        
    return render(request, 'search.html',{'books':books})
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# def sobre(request):
#     return HttpResponse("Teste Sobre")
    
    
    
## MODELO ANTIGO SEM OS COMENTÁRIOS:
## Só vai acessar os detalhes do livro se estiver autenticado
# def book_detail(request, id):
#     if request.user.is_authenticated:
#         book = Book.objects.get(id =id)
#         return render(request, 'book.html', {'book':book})  # {'book': book} é um dicionário sendo passado para o contexto da página que será renderizada.
#     else:
#         messages.error(request, 'Você precisa estar logado!')
#         return redirect('home')
    
    
    
    
    
    