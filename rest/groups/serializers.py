from rest_framework import serializers

from .models import Folder, File
from .defaults import DELIMITERS


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'path']


class FolderSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ['id', 'name', 'files']


class GroupFilesSerializer(serializers.Serializer):

    def validate_files(self, value):
        if not value or not isinstance(value, list):
            raise serializers.ValidationError("Invalid or missing files property in request data.")
        return value

    files = serializers.ListField(child=serializers.CharField(), help_text="List of file paths")
    delimiters = serializers.CharField(required=False, default=DELIMITERS, help_text="Optional string of delimiter characters")
