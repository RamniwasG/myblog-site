from django.db import models
from datetime import date
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

class Auther(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

class Post(models.Model):
    slug = models.SlugField(default="", null=False, db_index=True)
    title = models.CharField(max_length=100)
    image = models.URLField()
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE, null=True)
    updated_on = models.DateTimeField(null=True, default=date.today)
    # isActive = models.BooleanField(default=False)
    # rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
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