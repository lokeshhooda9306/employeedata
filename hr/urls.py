from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name= "index1"),
    path('update/<int:my_id>/', views.update , name ="updates" ),
]