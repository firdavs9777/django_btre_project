from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def register(request):
  if request.method =='POST':
    # Register  User
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      password2 = request.POST['password2']
      
      #Password Check 
      if password == password2:
        if User.objects.filter(username=username).exists():
          messages.error(request, 'That username is taken')
          return redirect('register')
        else: 
          if User.objects.filter(email=email).exists():
            messages.error(request, 'That email  is taken')
            return redirect('register')   
        # Create User
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, "You have successfully registered new user")
        return redirect('login')
      else: 
         messages.error(request, 'Passwords do not match')
         return redirect('register') 
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method =='POST':
    # Login User
    return render(request, 'accounts/login.html')
  else: 
    return render(request, 'accounts/login.html')

def logout(request):
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')