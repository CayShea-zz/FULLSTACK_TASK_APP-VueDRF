
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet


router = DefaultRouter()
router.register(r'/users', UserViewSet)
router.register(r'/tasks', TaskViewSet)


urlpatterns = router.urls