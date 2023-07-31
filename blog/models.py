from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super(Blog, self).save()

    def __str__(self) -> str:
        return f'{self.id}|     |{self.title}'
