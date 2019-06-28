# модели тестов

from django.db import models

from django_gii_pcmark.models.dicts import (
    OSDict, GPUDriversDict, DXVersionsDict, TestSoftDict,
    TestScreenSizeDict)
from django_gii_pcmark.models.hardware import System


class Mark(models.Model):
    """
    модель теста
    """

    system = models.ForeignKey(System, on_delete=models.CASCADE)

    test_soft = models.ForeignKey(TestSoftDict, on_delete=models.CASCADE)

    val_min = models.PositiveIntegerField()
    val_max = models.PositiveIntegerField(null=True, blank=True)
    val_avg = models.PositiveIntegerField(null=True, blank=True)
    val_dimension = models.CharField(max_length=10)

    os = models.ForeignKey(OSDict, on_delete=models.CASCADE, null=True, blank=True)

    gpu_driver = models.ForeignKey(GPUDriversDict, on_delete=models.CASCADE, null=True, blank=True)

    overclock_cpu_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_gpu_core_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_gpu_ram_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_ram_freq = models.PositiveIntegerField(null=True, blank=True)

    directx_version = models.ForeignKey(DXVersionsDict, on_delete=models.CASCADE, null=True, blank=True)

    comments = models.TextField(null=True, blank=True)

    url = models.URLField()

    screen_size = models.ForeignKey(TestScreenSizeDict, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Тесты систем'
        constraints = [
            models.UniqueConstraint(
                fields=['system', 'test_soft', 'screen_size'],
                name='mark_uniq'
            )
        ]