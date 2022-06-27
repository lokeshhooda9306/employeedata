from django.urls import path
from . import views


urlpatterns = [
      path('index/', views.MyView.as_view(), name="index"),
      path('update/<int:my_id>/', views.update_view.as_view() , name ="update" ),
      path('delete/<int:my_id>/', views.delete_view.as_view() , name ="delete" ),
]