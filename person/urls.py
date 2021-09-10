from django.urls import path
from person import views

urlpatterns = [
    path('singup/', views.signup_view, name='singup'),
]