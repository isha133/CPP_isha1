from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('contactus', views.contactus, name='contactus'),
    path('create', views.create, name='create'),
    path('read', views.read, name='read'),
    path('<str:emp_id>', views.update, name='update'),
    path('emloyees/<str:emp_id>', views.delete, name='delete'),
]