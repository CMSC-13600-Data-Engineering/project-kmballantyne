"""attendancechimp URL Configuration

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
from django.urls import include,path

from app import views

urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('new_submit', views.new_submit, name='new_submit'),
    path('createUser', views.createUser, name='createUser')
    # path('course_create', views.course_create, name='course_create'),
    # path('course_create_submit', views.course_create_submit, name='course_create_submit'),
    # path('qr_create', views.qr_create, name='qr_create'),
    # path('qr_create_submit', views.qr_create_submit, name='qr_create_submit'),
    # path('qr_upload', views.qr_upload, name='qr_upload'),
    # path('qr_upload_submit', views.qr_upload_submit, name='qr_upload_submit'),
    # path('handleform', views.handle_form, name='form')
]
