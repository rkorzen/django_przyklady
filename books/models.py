from django.db import models
from django.template.defaultfilters import slugify

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)

    def __repr__(self):
        return f"Author: {self.first_name} {self.last_name}"

    def __str__(self):
        return f"Author: {self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    # author = models.CharField(max_length=200)
    author = models.ForeignKey('books.Author', on_delete=models.CASCADE, related_name='books')
    year = models.SmallIntegerField()
    pages = models.IntegerField()
    slug = models.SlugField(null=True)


    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields
        )


    def __str__(self):
        return f"Book: {self.title} ({self.author})"
