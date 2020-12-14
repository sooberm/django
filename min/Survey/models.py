from django.db import models
from django.contrib.auth.models import AbstractUser



class UserCostume(AbstractUser):
    name2=models.CharField(max_length=100,null=True,blank=True)


class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    created_on = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_on']
    
class option(models.Model):
    name=models.CharField(max_length=100)
    question=models.ForeignKey(Question,on_delete=models.RESTRICT)

    rate=models.IntegerField(blank=True,default=0)
    def __str__(self):
        return f"{self.name}-{self.question}"