# модели тестов

from django.db import models

from django_gii_pcmark.models.dicts import (
    OSDict, GPUDriversDict, TestSoftDict, TestScreenSizeDict, ProducersDict, TestQualityDict,
    DXVersionsDict, AntiAliasingDict
)
from django_gii_pcmark.models.hardware import System


class Mark(models.Model):
    """
    модель теста
    """

    system = models.ForeignKey(System, on_delete=models.CASCADE)

    test_soft = models.ForeignKey(TestSoftDict, on_delete=models.CASCADE)
    test_soft_version = models.CharField(max_length=100, null=True, blank=True)
    test_quality = models.ForeignKey(TestQualityDict, null=True, blank=True, on_delete=models.CASCADE)
    directx_version = models.ForeignKey(DXVersionsDict, on_delete=models.CASCADE, null=True, blank=True)
    anti_aliasing_version = models.ForeignKey(AntiAliasingDict, on_delete=models.CASCADE, null=True, blank=True)

    val_min = models.PositiveIntegerField()
    val_max = models.PositiveIntegerField(null=True, blank=True)
    val_avg = models.PositiveIntegerField(null=True, blank=True)

    os = models.ForeignKey(OSDict, on_delete=models.CASCADE, null=True, blank=True)

    gpu_producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE, null=True, blank=True)
    gpu_model = models.CharField(max_length=50, null=True, blank=True)
    gpu_driver = models.ForeignKey(GPUDriversDict, on_delete=models.CASCADE, null=True, blank=True)

    overclock_cpu_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_gpu_core_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_gpu_ram_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_ram_freq = models.PositiveIntegerField(null=True, blank=True)

    comments = models.TextField(null=True, blank=True)

    url = models.URLField()

    screen_size = models.ForeignKey(TestScreenSizeDict, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        """
        строковое представление объекта
        :return:
        """
        return '{0} {1}'.format(self.test_soft, self.screen_size)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Тесты систем'
