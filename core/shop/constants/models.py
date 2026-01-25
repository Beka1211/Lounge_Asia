from django.db import models

class Base(models.Model):
    category = models.ForeignKey('shop.Category',  on_delete=models.CASCADE, related_name='dishes')
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание/Состав")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='dishes/', blank=True, verbose_name="Фото")

    def __str__(self):
        return f"{self.title} — {self.price} сом"