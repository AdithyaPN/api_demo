from django.urls import path,include
from . import views

# app_name='api_demo'
urlpatterns = [
    path('loaduser', views.load_user, name='loaduser'),
    path('adduser', views.add_user, name='adduser'),
    path('updateuser/<int:user_id>', views.update_user, name='updateuser'),
    path('deleteuser/<int:user_id>', views.delete_user, name='deleteuser'),
    path('index', views.index, name='index'),
    path('float', views.return_float, name='float'),
]