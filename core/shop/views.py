from rest_framework import views, generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DishSer, DishDetailSer, CategorySer
from .models import Category, Dish

class Home(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySer


class DishView(generics.ListAPIView):
    serializer_class = DishSer

    def get_queryset(self):
        queryset = Dish.objects.all()
        category = self.kwargs.get("category")

        if category:
            queryset = queryset.filter(category__slug=category)

        return queryset


class DishDetailView(generics.RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSer
    lookup_field = "slug"