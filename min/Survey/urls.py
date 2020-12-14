from django.contrib import admin
from .views import login_s,signup,Home,SureyDetail,submit
from django.urls import path
urlpatterns = [

path('signup/',signup,name='signup'),
path('login/',login_s,name='login'),
path('', Home.as_view(), name='home'),
path('surey-detail/<int:pk>',SureyDetail,name='SureyDetail'),
path('submit/<int:oid>',  submit , name = 'submit'),
]