"""god URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from system import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('contact/',views.contact,name = 'contact'),
    path('about/',views.about,name = 'about'),
    path('admin/profile/',views.admin_profile,name = 'admin_profile'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('student/registration/', views.student_registration, name='student_registration'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('login/',views.login_view,name='login_view'),
    path('a/login/',views.admin_login,name='admin_login'),
    path('post/list/',views.post_list,name='post_list'),
    path('leave/list/',views.leave_list,name='leave_list'),
    path('complaint/list/',views.complaint_list,name='complaint_list'),
    path('profile/',views.profile,name='profile'),
    path('leave/', views.leave_application, name='leave_application'),
    path('complaint/', views.complaint, name='complaint'),
   
    
]



