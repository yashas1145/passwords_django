from django.shortcuts import render
from add_password.models import password

# Create your views here.

def website(request):
    password_obj = password.objects.all()
    return render(request, 'website/index.html', {'pass': password_obj})