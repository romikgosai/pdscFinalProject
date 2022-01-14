from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField( max_length=50)
    desc = models.TextField(verbose_name="description")
    image = models.ImageField(upload_to="courses/")
    authorimage = models.ImageField(upload_to="courses/authors")

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField("",max_length=50)
    email = models.EmailField("")
    message = models.TextField("")

    def __str__(self):
        return self.name