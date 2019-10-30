from rest_framework.routers import DefaultRouter
from django.urls import path, include
from mystorage import views

router = DefaultRouter()
router.register('hjw_essay', views.PostViewSet)
router.register('hjw_album', views.ImgViewSet)
router.register('hjw_files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]