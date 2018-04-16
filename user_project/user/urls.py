from django.urls import path,include
from . import views
urlpatterns = [
    path('index/',views.index),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
]
