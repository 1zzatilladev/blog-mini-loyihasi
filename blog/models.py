from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blogs(models.Model):
    sarlovha=models.CharField(max_length=255,null=False)
    matn=models.CharField(max_length=255)
    muallif=models.CharField(max_length=255,null=False)
    yaratilgan_sana=models.DateField(auto_now_add=True)

def __str__(self):
        return f'{self.sarlovha}|{self.matn}' 