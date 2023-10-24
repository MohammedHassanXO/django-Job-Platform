from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone 
from django.utils.text import slugify


#job-type tuple
JOB_TYPE = (    ('FullTime', 'FullTime'), ('PartTime', 'ParTime'), ('Remote', 'Remote'), ('Freelance', 'Freelance')   )


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=120)
    location = CountryField()
    created_at = models.DateTimeField(default=timezone.now)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='job_company')
    salary_start = models.IntegerField(null=True, blank=True)
    salary_end = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=15000)
    vacancy = models.IntegerField()
    job_type = models.CharField(choices=JOB_TYPE, max_length=10)
    experience = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='job_category', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs) #call the real save() method
    



class Category(models.Model):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name




class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=1000)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name