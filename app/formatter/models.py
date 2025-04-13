from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Query(models.Model):
    raw_Query = models.TextField()
    formatted_Query =  models.TextField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.formatted_Query or self.raw_Query