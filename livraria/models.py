from django.db import models
from django.contrib.auth.models import User



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
    
    def __str__(self):
        return(f'{self.title}-{self.value}')
    
    
    
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300) # Limita o numero de caracteres a serem armazenados no banco de dados
    
    def __str__(self):
        return f"Comentário de {self.user.username} para {self.book.title}"
    
    










