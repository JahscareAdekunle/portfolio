from django.db import models

# Create your models here.
class Message(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  subject = models.CharField(max_length=500)
  message = models.TextField()
  def __str__(self):
    return self.subject
    
class Category(models.Model):
  title = models.CharField(max_length= 255)
  slug = models.SlugField()
  
  def __str__(self):
    return self.title
    
  class Meta:
    ordering = ("-title",)
  
class Post(models.Model):
  category = models.ForeignKey(Category ,on_delete = models.CASCADE)
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  created_at = models.DateTimeField(auto_now_add=True)
  intro = models.CharField(max_length=255)
  body = models.TextField()
  
  def __str__(self):
    return self.title
 
  class Meta:
    ordering = ("-created_at",)
    
    
    
class Comment(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ("created_at",)
  
  def __str__(self):
    return self.body