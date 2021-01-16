from django.urls import path

from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('home/<int:user_id>', index, name='home'),
    path('home/update_like/<int:pk>/<int:user_id>', update_like, name='update_like')
]
