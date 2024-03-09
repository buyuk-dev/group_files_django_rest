# groups/views.py

from rest_framework import viewsets
from .models import Folder, File
from .serializers import FolderSerializer, FileSerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
