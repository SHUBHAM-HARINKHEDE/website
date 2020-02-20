from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')



    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Education(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    college=models.CharField(max_length=300)
    board=models.CharField(max_length=300)
    qualification=models.CharField(max_length=100)
    grade=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username}-{self.qualification}'

class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=500)
    subject=models.CharField(max_length=500)
    message=models.TextField()

    def __str__(self):
        return self.email
    

    




