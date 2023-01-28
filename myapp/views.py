from django.shortcuts import render
from .models import Message 
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