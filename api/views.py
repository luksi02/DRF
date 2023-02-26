from wsgiref.util import FileWrapper
from api.custom_renderers import JPEGRenderer, PNGRenderer
from rest_framework import generics, mixins, permissions, authentication, request
from images.models import Images
from .serializers import ImagesSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import StaticHTMLRenderer
from django.http import HttpResponse
from PIL import Image
from .permissions import Basic, Premium, Enterprise, Admin


class ImageAPIView(generics.RetrieveAPIView):

    queryset = Images.objects.filter(id=1)
    renderer_classes = [JPEGRenderer, PNGRenderer]
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        renderer_classes = [JPEGRenderer]
        queryset = Images.objects.get(id=self.kwargs['id']).image
        data = queryset
        return Response(data, content_type='image/jpg')

class ImagesListAPIView(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    renderer_classes = [JPEGRenderer, PNGRenderer]

    def get(self, request, *args, **kwargs):

        queryset = Images.objects.filter(author=request.user.id)
        data = queryset
        return Response(data, content_type='image/jpg')


class ImagesListAPIView2(APIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    renderer_classes = [JPEGRenderer, PNGRenderer]

    def get(self, request, *args, **kwargs):

        queryset = Images.objects.filter(author=request.user.id)
        data = queryset
        return Response(data, content_type='image/jpg')
