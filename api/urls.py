from django.urls import path
from .views import ImageAPIView, ImagesListAPIView, ImagesListAPIView2

#from . import views

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('images_list', ImagesListAPIView.as_view()),
    path('images_list2', ImagesListAPIView2.as_view()),
    path('id/<id>', ImageAPIView.as_view()),
    #path('', views.ImageAPI, name='post_single'),
]
