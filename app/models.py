from django.db import models

# Create your models here.
class Super_AdminAccount(models.Model):

   
    Fname=models.CharField(max_length=255, default="First Name")
    Profile= models.ImageField(upload_to='SuperAdmin/',default="SuperAdmin/dummy.jpg")
    def __str__(self):
        return self.Fname