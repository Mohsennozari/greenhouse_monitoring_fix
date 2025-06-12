from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class GreenhouseData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.FloatField(verbose_name="دما (سانتی‌گراد)")
    humidity = models.FloatField(verbose_name="رطوبت (درصد)")
    light = models.FloatField(verbose_name="نور (لوکس)")
    recorded_at = models.DateTimeField(default=timezone.now, verbose_name="زمان ثبت")

    class Meta:
        verbose_name = "داده گلخانه"
        verbose_name_plural = "داده‌های گلخانه"

    def __str__(self):
        return f"داده {self.user.username} در {self.recorded_at}"