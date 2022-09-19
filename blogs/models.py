from django.db import models
from datetime import date
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    slug = models.SlugField(default="", null=False, db_index=True)
    title = models.CharField(max_length=100)
    image = models.URLField()
    auther = models.CharField(max_length=100)
    updated_on = models.DateTimeField(null=True, default=date.today)
    # isActive = models.BooleanField(default=False)
    excerpt = models.CharField(max_length=200)
    content = models.CharField(null=True, max_length=1000)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail-page', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)