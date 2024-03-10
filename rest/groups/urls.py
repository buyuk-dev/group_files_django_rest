from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FolderViewSet, FileViewSet, GroupFilesView


router = DefaultRouter()
router.register(r'folders', FolderViewSet)
router.register(r'files', FileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('group-files/', GroupFilesView.as_view(), name='group-files')
]
