from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.utils.text import slugify

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Auther(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_fullname(self):
        return self.get_fullname()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(default='', max_length=100)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    auther = models.ForeignKey(
        Auther, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag) # allows to setup MANY_TO_MANY RELATION
    
    # Optional fields
        # isActive = models.BooleanField(default=False)
        # rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail-page', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)