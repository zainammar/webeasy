from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)

    image1 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image2 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image3 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image4 = models.ImageField(upload_to='pages/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
