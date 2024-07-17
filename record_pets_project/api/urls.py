from django.urls import include, path

from .routers import CustomRouter
from .views import PetViewSet

router = CustomRouter()

router.register(r'pets', PetViewSet, basename='pet')

urlpatterns = [
    path('', include(router.urls)),
]
