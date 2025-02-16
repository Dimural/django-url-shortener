from django.urls import path
from .views import home, redirect_url, delete_url

urlpatterns = [
    path('', home, name='home'), #this is the home page of the website
    path('<str:short_code>/', redirect_url, name='redirect_url'), #this is the redirect url function
    path('<str:short_code>/delete/', delete_url, name='delete_url'), #this is the delete url function
]
