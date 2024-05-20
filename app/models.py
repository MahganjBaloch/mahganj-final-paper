from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class blogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    pubDate = models.DateField()
    author = models.ForeignKey(Author , on_delete=models.CASCADE )

    def __str__(self):
        return self.title
    
    




