from django.db import models

# Create your models here.
class Message(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  subject = models.CharField(max_length=500)
  message = models.TextField()
  def __str__(self):
    return self.subject