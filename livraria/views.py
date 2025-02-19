from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from .forms import SignUpForm, AddBookForm, CommentForm, RatingForm
# from .forms import SignUpForm, AddBookForm, CommentForm, RatingForm, ProfileForm
from .models import Book, Comment, RatinStar, UserProfile, Cart, CartItem
from django.template.loader import render_to_string



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
            messages.success(request, f'Olá {user.username}, Seja Bem Vindo! ')
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
            user = form.save() # Salvando o objeto usuario na variavel user para utilizar na variavel user user_profile
            user_image = form.cleaned_data['user_image']
            cpf = form.cleaned_data['cpf']
            
            if user_image:
                user_profile = UserProfile.objects.create(user = user, user_image = user_image, cpf = cpf)
            else:
                # user_profile = UserProfile.objects.create(user = user,  user_image = "../../media/users/default.jpg" , cpf = cpf)
                user_profile = UserProfile.objects.create(user = user,  user_image = "users/default.jpg" , cpf = cpf)
                
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


def profile_user_view(request, id):
    if request.user.is_authenticated:
        books = Book.objects.all()

        user_logged = request.user  # Usuário logado
        user_profile = get_object_or_404(User, id=id)  # Usuário visitado
        ratings = RatinStar.objects.filter(user=user_profile).order_by('-rating')        
        
        # Remover avaliações duplicadas por livro ( Não da pra fazer com set pois se não vai ser perdido as propriedades de busca )
        unique_ratings = []
        seen_books = set()
        for rating in ratings:
            if rating.book not in seen_books: # Se o livro não existe em seen_books (livros vistos)
                unique_ratings.append(rating)
                seen_books.add(rating.book) # adiciona a livros vistos impedindo que ocorra repetições de itens
            if len(unique_ratings) == 5:
                break
            
        # Remover generos repetidos
        unique_genres = set()
        for rating in ratings:
            unique_genres.add(rating.genre)           
             
        form = SignUpForm(request.POST or None, instance=user_profile)

        return render(request, 'profile_view.html', {
            'user_logged': user_logged,  # Sempre mantém o usuário logado separado
            'user_profile': user_profile,  # Usuário cujo perfil está sendo visitado
            'form': form,
            "ratings": unique_ratings,
            "books": books,
            "unique_genres": unique_genres,
            # "unique_ratings_index": unique_ratings_index,
        })
    else:
        return redirect('home')
    
    
def profile_user_edit(request):
    return redirect(request, 'profile_view')
    # if request.user.is_authenticated:
    #     user = request.user
    #     user_profile = UserProfile.objects.filter(user=user).first() # apenas o primeiro registro encontrado vai ser retornado
    #     form = ProfileForm(request.POST or None, request.FILES or None, instance=user)
        
    #     if user_profile:
    #         form.fields['cpf'].initial = user_profile.cpf
    #         form.fields['user_image'].initial = user_profile.user_image
            
    #     if request.method == 'POST':
    #         if form.is_valid():
    #             form.save()
                
    #             user_profile.cpf = form.cleaned_data['cpf']
    #             user_profile.user_image = form.cleaned_data['user_image']
    #             user_profile.save()  # Salva as alterações no perfil
                
    #             # # Atualiza o perfil do usuário com o campo cpf
    #             # if user_profile:
    #             #     user_profile.cpf = form.cleaned_data['cpf']
    #             #     user_profile.save()
                    
    #             messages.success(request, "Perfil Atualizado!")
    #             return redirect('profile_view')
    #         else:
    #             messages.error(request,'Erro ao atualizar o perfil. Tente novamente.')

    #     # No caso de GET ou falha no formulário, renderiza o formulário
    #     return render(request, 'profile_edit.html', {'form': form})
    
    # else:
    #     return redirect('home')


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
                        rating.genre = book.genre
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




def get_cart_context(request):
    cart_user = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart= cart_user)
    return{'cart_user':cart_user, 'cart_items':cart_items}



def add_cart(request,book_id):
    # book = Book.objects.get(id=book_id)
    # cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Pega o livro que foi clicado
    book = get_object_or_404(Book, id=book_id)
    
    # Recupera ou cria o carrinho para o usuário
    cart, created = Cart.objects.get_or_create(user=request.user)
        
    # Verifica se ja existe o item no carrinho:
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    context_cart = get_cart_context(request)
    
    # modal_html = render_to_string("modal_cart_add.html",context_cart)
    # return JsonResponse({'modal_html':modal_html})

    return render(request,'modal_cart_add.html', context_cart)
    # return {'context_cart': context_cart}



def view_cart(request):
    # cart_user = Cart.objects.get(user=request.user)
    context_cart = get_cart_context(request)
    return render(request, 'modal_cart_nav.html',{'context_cart': context_cart})
        
        
        
        
        
        
        
        
        
        
        



        
        # Remover avaliações duplicadas por livro ( Não da pra fazer com set pois se não vai ser perdido as propriedades de busca )
        # unique_ratings = []
        # unique_ratings_index = []   
        # seen_books = set()
        # for i,rating in enumerate(ratings):
        #     if rating.book not in seen_books: # Se o livro não existe em seen_books (livros vistos)
        #         unique_ratings.append(rating)
        #         seen_books.add(rating.book) # adiciona a livros vistos impedindo que ocorra repetições de itens
        #         unique_ratings_index.append(i)
        #     if len(unique_ratings) == 5:
        #         break
        
        
        
        
        
        
        
        
        
        
        
        

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
    
    
    
    
    
    