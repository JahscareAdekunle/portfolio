from django.shortcuts import render
#get_objects_or_404
from .models import Message ,Post, Comment 

# Create your views here.
def index(request):
  if request.method == "POST":
    name = request.POST["name"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    body = request.POST["Message"]
    
    message = Message(name=name,email=email, subject=subject, message=body)
    message.save()
  
    
  return render(request,'myapp/index.html',{})
  
def post(request):
  post = Post.objects.all()
  return render(request,'myapp/blog.html',{"blog":post})
  
def detail(request,slug):
  post = Post.objects.get(slug=slug)
  return render(request,'myapp/detail.html',{'post':post})
  