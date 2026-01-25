from django.db import models
from shop.constants.models import Base

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Категория")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Dish(Base):
    slug = models.SlugField(unique=True)
    weight = models.PositiveIntegerField(null=True, blank=True, verbose_name="Вес (г)")

    def __str__(self):
        return f"{self.title} - {self.price} сом."


class Desert(Base):
    pass

class Macaron(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="Макароны")



class Drink(Base):
    volume = models.PositiveIntegerField(verbose_name="Объём (мл)")