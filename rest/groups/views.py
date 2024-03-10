from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from drf_yasg.utils import swagger_auto_schema


from .models import Folder, File
from .serializers import FolderSerializer, FileSerializer, GroupFilesSerializer
from .utils import group_files
from .defaults import DELIMITERS


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


class GroupFilesView(APIView):

    class GroupFilesSchema(AutoSchema):
        def get_request_body(self, path, method):
            return {
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'files': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'delimiters': {
                                    'type': 'string',
                                    'default': DELIMITERS
                                }
                            },
                            'required': ['files']
                        }
                    }
                }
            }

    schema = GroupFilesSchema()

    @swagger_auto_schema(request_body=GroupFilesSerializer)
    def post(self, request, *args, **kwargs):

        serializer = GroupFilesSerializer(data=request.data)

        if serializer.is_valid():
            grouped_files = group_files(
                serializer.validated_data.get('files'),
                serializer.validated_data.get('delimiters')
            )
            return Response(grouped_files, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
