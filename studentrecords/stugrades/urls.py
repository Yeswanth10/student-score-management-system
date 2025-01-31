from django.urls import path

from stugrades import views


urlpatterns = [
    path('',views.home),
    path('read',views.read)
]