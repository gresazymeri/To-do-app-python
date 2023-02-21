from django.db import models

class Task(models.Model):
    user_id = models.IntegerField(default=0)
    title=models.TextField(max_length=255,default='')
    due_date = models.DateField()
    done = models.BooleanField(default=False)

  
