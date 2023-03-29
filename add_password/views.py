from django.shortcuts import render, redirect
from .models import password as pw

# Create your views here.

def add_password(request):
    return render(request, 'add_password/index.html', {})

def post_password_model(request):
    
    if request.method == 'POST':
        temp = pw()
        temp.url = request.POST['url']
        temp.password = request.POST['password']
        
        temp.save()
        return redirect('/')
    
def del_password(request, my_value):
    temp = pw.objects.get(pk=my_value)
    temp.delete()
    return redirect('/')