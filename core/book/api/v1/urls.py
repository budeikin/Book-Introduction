from rest_framework.routers import DefaultRouter
from .views import BookViewSet, GenreViewSet, WriterViewSet

app_name = 'book_api'

router = DefaultRouter()
router.register('book', BookViewSet, basename='book')
router.register('genre', GenreViewSet, basename='genre')
router.register('writer', WriterViewSet, basename='writer')
urlpatterns = router.urls
