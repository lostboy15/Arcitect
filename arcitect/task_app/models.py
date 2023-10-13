from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  COMPLETE = "Complete"
  PENDING = "Pending"
  STATUS = [
    (COMPLETE, "Complete"),
    (PENDING, "Pending")
  ]

  task_id = models.CharField(max_length=200,null=False, blank=False)
  title = models.CharField(max_length=200,null=False,blank=False)
  description = models.TextField(null=True, blank=True)
  status = models.CharField(max_length=200, choices=STATUS,default=PENDING)
  user = models.ForeignKey(User,max_length=10,on_delete=models.CASCADE,null=True)

  