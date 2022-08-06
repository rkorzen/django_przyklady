from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author = models.ForeignKey('articles.Author', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return f"Article: {self.title} {self.author}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    def __repr__(self):
        return f"Author: {self.first_name} {self.last_name}"

    def __str__(self):
        return f"Author: {self.first_name} {self.last_name}"

