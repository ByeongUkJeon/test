from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router=DefaultRouter()
router.register('user',views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.signup),
    path('login/', views.login),
    path('idCheck/', views.idCheck),
    path('nickCheck/', views.nicknameCheck),
    path('addTale/', views.addTale)
]