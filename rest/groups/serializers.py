# groups/serializers.py

from rest_framework import serializers
from .models import Folder, File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'path']

class FolderSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ['id', 'name', 'files']
