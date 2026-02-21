from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    category = models.ManyToManyField(Category) #ekta post multiple catgory er majhe thakte pare, abr ekta post er vitor multiple category thakte pare
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title