from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet, BioModelViewSet, CityModelViewSet
from facebook.views import FacebookModelViewSet, ToDoModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('bio', BioModelViewSet)
router.register('city', CityModelViewSet)
router.register('facebook', FacebookModelViewSet)
router.register('todo', ToDoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
