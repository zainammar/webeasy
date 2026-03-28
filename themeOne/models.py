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
    content5 = models.TextField(blank=True)
    content6 = models.TextField(blank=True)
    content7 = models.TextField(blank=True)
    content8 = models.TextField(blank=True)

    image1 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image2 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image3 = models.ImageField(upload_to='pages/', blank=True, null=True)
    image4 = models.ImageField(upload_to='pages/', blank=True, null=True)


    content9 = models.TextField(blank=True)
    content10 = models.TextField(blank=True)
    content11 = models.TextField(blank=True)
    content12 = models.TextField(blank=True)
    content13 = models.TextField(blank=True)
    content14 = models.TextField(blank=True)
    content15 = models.TextField(blank=True)
    content16 = models.TextField(blank=True)

    content17 = models.TextField(blank=True)
    content18 = models.TextField(blank=True)
    content19 = models.TextField(blank=True)
    content20 = models.TextField(blank=True)
    content21 = models.TextField(blank=True)
    content22 = models.TextField(blank=True)
    content23 = models.TextField(blank=True)
    content24 = models.TextField(blank=True)

    content25 = models.TextField(blank=True)
    content26 = models.TextField(blank=True)
    content27 = models.TextField(blank=True)
    content28 = models.TextField(blank=True)
    content29 = models.TextField(blank=True)
    content30 = models.TextField(blank=True)
    content31 = models.TextField(blank=True)
    content32 = models.TextField(blank=True)

    GRID_CHOICES2 = (
    
        ('col-1', '1 Column'),
        ('col-2', '2 Columns'),
        ('col-3', '3 Columns'),
        ('col-4', '4 Columns'),
    )
    css_file = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    