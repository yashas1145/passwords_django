from django.shortcuts import render, redirect
from add_password.models import password as pw

# Create your views here.

def upd_password(request, my_value):
    temp = pw.objects.get(pk=my_value)
    return render(request, 'upd_password/index.html', {'url': temp, 'id':my_value})

def save_password(request, my_value):
    
    if request.method == 'POST':
        url = request.POST['url']
        pwd = request.POST['password']
        
        obj = pw.objects.get(pk=my_value)
        obj.url = url
        obj.password = pwd
        obj.save()
        
    return redirect('/')