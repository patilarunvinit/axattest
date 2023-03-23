
from django.db import models

class reg(models.Model):
    email=models.CharField(max_length=100,null=True,unique=True)
    option=models.CharField(max_length=60,null=True)
    mobile_no=models.CharField(max_length=14,null=True)


    objects = models.Manager()



def image_upload_to(instance, filename):
    # You can access to your model fields with instance for example: instance.name
    name=instance.email
    image=instance.image
    return f'images/{name}/{image}'

class data(models.Model):
    image = models.ImageField(upload_to=image_upload_to, null=True)
    email=models.CharField(max_length=100,null=True)
    print(email)
    option=models.CharField(max_length=60,null=True)


    objects = models.Manager()

