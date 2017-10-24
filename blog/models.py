from django.db import models
from django.db.models import permalink

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.TextField()
    image = models.CharField(max_length=100,unique=False,default='default.png')
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __str__(self):
       return '{}'.format(self.title)

    def url(self):
        return reverse('view_post', args=[self.slug])

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
       return '{}'.format(self.title)

    def url(self):
        return reverse('view_category', args=[self.slug])
