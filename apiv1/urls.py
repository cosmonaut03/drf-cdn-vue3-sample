from django.urls import include, path
from rest_framework import routers

from apiv1.views import user_views

from .views import book_views
from .views import artist_views

router = routers.DefaultRouter()
router.register("books", book_views.BookViewSet)

app_name = "apiv1"
urlpatterns = [
    path("", include(router.urls)),
    path("artists/", artist_views.ArtistListCreateView.as_view()),
    path("artists/<pk>", artist_views.ArtistListCreateView.as_view()),
    path("user/<id>", user_views.UserRetriveUpdateDeleteView.as_view()),
]
