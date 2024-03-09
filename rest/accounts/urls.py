from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserListView


router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/list/', UserListView.as_view(), name='user-list'),
]
