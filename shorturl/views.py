from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import URL
from django.contrib import auth
from django.contrib.auth import logout as auth_logout
import uuid
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        urls_user = URL.objects.filter(user=request.user)
        context = {'urls':urls_user}
        return render(request, 'index.html', context)
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def create(request):
    if request.method == 'POST':
        long_url = request.POST.get('longurl')
            
        uid = str(uuid.uuid4())[:7]
        shorten_url = f'localhost:8000/{uid}'
            
        instance = URL(longurl=long_url, shortenurl=shorten_url, user =request.user, uuid=uid)
        instance.save()
        return redirect('/')
    return render(request, 'create_url.html')

def logout(request):
    if request.user:
        auth_logout(request)
    return redirect('/')

def open(request, pk):
    url_object = URL.objects.filter(uuid=pk).values_list('longurl').last()
    final_url = ''
    for i in url_object:
        if i not in "'()":
            final_url += i
    return redirect(final_url)
    # but i dont know why its working for return redirect(i)