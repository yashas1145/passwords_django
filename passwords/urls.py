"""passwords URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import website
from add_password.views import add_password, post_password_model, del_password
from upd_password.views import upd_password, save_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', website, name='website'),
    path('add_password', add_password, name='add_password'),
    path('add_pass', post_password_model, name='post_password_model'),
    path('del_pass/<int:my_value>', del_password, name='del_password'),
    path('upd_pass/<int:my_value>', upd_password, name='upd_password'),
    path('save_pass/<int:my_value>', save_password, name='save_password'),
]
