
from rest_framework.routers import DefaultRouter

from app.ws import views as images_views

router = DefaultRouter()

router.register('images', images_views.ImagesViewSet, basename='images')


app_name = 'api'
urlpatterns = router.urls
