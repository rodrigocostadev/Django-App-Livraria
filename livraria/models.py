from django.db import models
from django.contrib.auth.models import User
# from star_ratings.models import Rating


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
    # rating = models.ForeignKey(Rating, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return(f'{self.title}-{self.value}')
    
    
    
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300) # Limita o numero de caracteres a serem armazenados no banco de dados
    
    def __str__(self):
        return f"Comentário de {self.user.username} para {self.book.title}"
    
    
    
class RatinStar(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # rating = models.IntegerField()
    
    rating = models.DecimalField(
        max_digits=3,    # Número total de dígitos (antes e depois do ponto decimal)  "numero ponto numero"
        decimal_places=1, # Número de casas decimais após o ponto
        )
    
    def __str__(self):
        return f"Avaliação de {self.user} para o livro: {self.book.title}"
    
    
    
    










