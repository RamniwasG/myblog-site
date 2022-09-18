from django.db import models
from datetime import date
class Post(models.Model):
    slug = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    image = models.URLField()
    auther = models.CharField(max_length=100)
    updated_on = models.CharField(max_length=50, default=date.today)
    # isActive = models.BooleanField(default=False)
    excerpt = models.CharField(max_length=200)
    content = models.CharField(null=True, max_length=1000)

    def __str__(self):
        return self.title

    def create_post(self):
        pass