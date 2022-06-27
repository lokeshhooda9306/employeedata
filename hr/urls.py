from django.urls import path
from . import views


urlpatterns = [
      path('index/', views.MyView.as_view(), name="index"),
      path('update/<int:pk>/', views.MyViewUpdate.as_view(), name="update"),
      path('delete/<int:pk>/', views.MyViewDelete.as_view(), name="delete"),



]