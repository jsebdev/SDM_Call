from django.urls import path
from . import views

urlpatterns = [
    # path('get_calls', views.getCalls),
    # path('sd_call/', views.call)
    path('call/', views.call)
]
