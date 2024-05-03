from django.urls import path

from . import views

urlpatterns = [
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
