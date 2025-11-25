from django.db import models
from django.conf import settings

from units_center.models import Unit

# Create your models here.


class Booking(models.Model):
    STATUS_CHOICES = [
        ("requested", "طلب جديد"),
        ("confirmed", "مؤكد"),
        ("rejected", "مرفوض"),
    ]

    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings", verbose_name="المستأجر")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="bookings", verbose_name="الوحدة")
    start_date = models.DateField(verbose_name="تاريخ البداية")
    end_date = models.DateField(verbose_name="تاريخ النهاية")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="requested", verbose_name="الحالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    notes = models.TextField(blank=True, verbose_name="ملاحظات")

    def __str__(self) -> str:
        return f"حجز {self.unit} للمستخدم {self.tenant_id} من {self.start_date} إلى {self.end_date}"

    class Meta:
        verbose_name = "حجز"
        verbose_name_plural = "الحجوزات"
