from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('update_like/<int:pk>', update_like, name='update_like')
]
