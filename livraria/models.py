from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to="users", blank=True, null=True)
    # cpf = models.IntegerField(unique=True, null=False)
    # cpf = models.IntegerField(null=False)
    cpf = models.CharField(max_length=11,null=False)


class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    value = models.FloatField()
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images")
    media_rating = models.DecimalField(default=0, max_digits=3, decimal_places=1, )
    
    def __str__(self):
        return(f'{self.title}-{self.value}')



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Carrinho de {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.book.title}"
    
    def total_price(self):
        return self.book.value * self.quantity
    
    
    
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300) # Limita o numero de caracteres a serem armazenados no banco de dados
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comentário de {self.user.username} para {self.book.title}"
    
    
    
class RatinStar(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    n_review = models.IntegerField(default=0)
    genre = models.CharField(max_length=100)
    # media_rating = models.DecimalField(default=0,max_digits=3,decimal_places=1,)     COLOCAR MEDIA DE RATING
    # rating = models.IntegerField()    
    
    rating = models.DecimalField(
        max_digits=3,    # Número total de dígitos (antes e depois do ponto decimal)  "numero ponto numero"
        decimal_places=1, # Número de casas decimais após o ponto
        )
    
    def __str__(self):
        return f"Avaliação de {self.user} para o livro {self.book.title} ({self.book.genre}), nota: {self.rating} / numero de avaliações: {self.n_review}"
    
    
    
    










