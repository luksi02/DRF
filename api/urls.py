from django.urls import path
from .views import ImageAPIView, ImagesListAPIView, ImagesListAPIView2, ImageUploadView

#from . import views

urlpatterns = [
    path('', ImageAPIView.as_view(), name='index'),
    path('images_list', ImagesListAPIView.as_view()),
    path('images_list2', ImagesListAPIView2.as_view()),
    path('id/<id>', ImageAPIView.as_view()),
    path('upload/', ImageUploadView.as_view(), name='upload'),
    #path('', views.ImageAPI, name='post_single'),
]
