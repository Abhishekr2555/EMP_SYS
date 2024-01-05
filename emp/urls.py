"""
URL configuration for emp_ms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


# name=>html page name
# views.function=> which is views.py
# ''=>slug which url when type to search
# at last not required '/' in path('')

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='home'),  #home with Otp login
    path('home', views.home,name='home'),   #normal home lending page
    path('login/', views.loginpage, name='login'),
    path('logout', views.logoutpage,name='logout'),
    path('login1',views.login1,name='login1'),
    path('otp',views.otp,name='otp'),
    path('', views.sign, name='signup'),                                         
    path('index', views.index,name='index'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('remove_emp/', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('d_emp', views.d_emp, name='d_emp'),
    path('contect', views.contect, name='contect'),
    path('about', views.about, name='about')
    # path('qrcode/', views.qrcode, name='qrcode'),
    ]
