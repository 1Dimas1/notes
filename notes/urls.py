from django.urls import path
from . import views

urlpatterns = [
    path('greeting/', views.greeting),
    path('routine/', views.routine),

]
