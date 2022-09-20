from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class ProgrammingLang(models.Model):
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language


class Technology(models.Model):
    technology = models.CharField(max_length=60)
    
    def __str__(self):
        return self.technology


class Developer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_fullname(self):
        return self.get_fullname()


class Period(models.Model):
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now) 

    def __str__(self):
        return f"{self.start_date} to {self.end_date}"


class Projects(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True)
    excerpt = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    image_name = models.CharField(default='', max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    description = models.TextField(validators=[MinLengthValidator(10)])
    # related Models
    tags = models.ManyToManyField(Tag) # App Type - (website, mobile app, desktop app)
    technologies = models.ManyToManyField(Technology) # React/Angular/Django/SAP UI5
    languages = models.ManyToManyField(ProgrammingLang) # JavaScript/Java/Python/Perl/C/C++
    developed_by = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True, related_name="projects")    
    
    status = models.CharField(max_length=20) # completed, in-progress
    employer = models.CharField(max_length=200)
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail-page', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)