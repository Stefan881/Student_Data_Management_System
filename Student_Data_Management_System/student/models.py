from django.db import models

# Create your models here.

class Student(models.Model):
    Registration_No = models.CharField(max_length=25,default=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email =  models.EmailField(max_length=50)
    National_ID = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)
    Profile_photo = models.ImageField(null=True,blank=True,upload_to="images/")


    def __str__(self):
        return (f"{self.first_name}{self.last_name}")


class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email