from asyncore import file_dispatcher
from files.models import File
from files.serializers import FileSerializer
from rest_framework import generics#, permissions
from django.contrib.auth.models import User
# from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

class FileRootList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileList(generics.ListCreateAPIView):
    lookup_field = 'path'
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'files': reverse('file-root-list', request=request, format=format)
    })
