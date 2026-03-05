from django.db import models

class Page(models.Model):

    GRID_CHOICES = (
        # ('1col', '1 Column'),
        # ('2col', '2 Columns'),
        # ('3col', '3 Columns'),
        # ('4col', '4 Columns'),

        ('col-1', '1 Column'),
        ('col-2', '2 Columns'),
        ('col-3', '3 Columns'),
        ('col-4', '4 Columns'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    grid_layout = models.CharField(
        max_length=10,
        choices=GRID_CHOICES,
        default='2col'
    )

    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)

    image1 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image2 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image3 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image4 = models.ImageField(upload_to='pages/', blank=True, null=True)


    content5 = models.TextField(blank=True)
    content6 = models.TextField(blank=True)
    content7 = models.TextField(blank=True)
    content8 = models.TextField(blank=True)


    GRID_CHOICES2 = (
        # ('1col', '1 Column'),
        # ('2col', '2 Columns'),
        # ('3col', '3 Columns'),
        # ('4col', '4 Columns'),

        ('col-1', '1 Column'),
        ('col-2', '2 Columns'),
        ('col-3', '3 Columns'),
        ('col-4', '4 Columns'),
    )
    css_file = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    