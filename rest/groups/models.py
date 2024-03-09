from django.db import models
from django.conf import settings

class Folder(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='folders')

    def __str__(self):
        return self.name

class File(models.Model):
    path = models.CharField(max_length=1024)  # Assuming file paths are stored as strings
    folder = models.ForeignKey(Folder, related_name='files', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.path
