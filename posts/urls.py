from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list),
    path('comment/', views.comment_list),
]
