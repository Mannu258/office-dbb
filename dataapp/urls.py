from django.urls import path,re_path
from . views import *

urlpatterns = [
    path('', index,name="home"),
    path('details/<id>',details,name="details")
    
]
