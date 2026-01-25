from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (Home, DishView, DishDetailView)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("menu/", DishView.as_view(), name="menu"),
    path("menu/<slug:category>/", DishView.as_view(), name="menu_category"),
    path("menu/<slug:slug>/", DishDetailView.as_view(), name="specific_dish"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
