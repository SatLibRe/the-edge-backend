from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),         # GET and POST
    path('<int:pk>/', views.post_detail, name='post_detail'),  # GET, PUT, DELETE
]
