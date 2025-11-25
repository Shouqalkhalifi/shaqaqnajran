from django.db import models
from django.conf import settings

# Create your models here.


class Unit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="units", verbose_name="المالك")
    name = models.CharField(max_length=150, verbose_name="اسم الوحدة")
    description = models.TextField(blank=True, verbose_name="الوصف")
    city = models.CharField(max_length=100, default="نجران", verbose_name="المدينة")
    address = models.CharField(max_length=255, blank=True, verbose_name="العنوان")
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="سعر الليلة")
    is_active = models.BooleanField(default=True, verbose_name="مفعّلة")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "وحدة سكنية"
        verbose_name_plural = "الوحدات السكنية"
