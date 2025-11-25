from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Profile(models.Model):
    ROLE_CHOICES = [
        ("tenant", "مستأجر"),
        ("owner", "مالك وحدة"),
        ("operator", "مشغّل المنصة"),
    ]

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profile", verbose_name="المستخدم")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="tenant", verbose_name="الدور")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="رقم الجوال")

    def __str__(self) -> str:
        return f"{self.user.username} ({self.get_role_display()})"

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"
