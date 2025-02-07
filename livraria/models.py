from django.db import models



class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    value = models.FloatField()
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return(f'{self.title}-{self.value}')
    










