from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Greenhouse(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام گلخانه")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="greenhouses", verbose_name="مالک")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="زمان ایجاد")

    class Meta:
        verbose_name = "گلخانه"
        verbose_name_plural = "گلخانه‌ها"

    def __str__(self):
        return f"{self.name} ({self.owner.username})"

class GreenhouseData(models.Model):
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE, related_name="data", verbose_name="گلخانه")
    temperature = models.FloatField(verbose_name="دما (سانتی‌گراد)")
    humidity = models.FloatField(verbose_name="رطوبت (درصد)")
    light = models.FloatField(verbose_name="نور (لوکس)")
    recorded_at = models.DateTimeField(default=timezone.now, verbose_name="زمان ثبت")

    class Meta:
        verbose_name = "داده گلخانه"
        verbose_name_plural = "داده‌های گلخانه"

    def __str__(self):
        return f"داده {self.greenhouse.name} در {self.recorded_at}"