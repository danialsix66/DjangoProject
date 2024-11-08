from django.db import models
from django.urls import reverse
from .validators import validate_file_size

class Book(models.Model):
    user=models.ForeignKey('auth.User' ,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    translator=models.CharField(max_length=100 , blank=True)
    description=models.TextField()
    price=models.PositiveIntegerField()   
    cover=models.ImageField(upload_to='covers/' , blank = True , null=True , validators=[validate_file_size])


    def __str__(self):
        return f"{self.title} : {self.author}"

    def get_absolute_url(self):
        return reverse('book_detail' , args=[self.id])