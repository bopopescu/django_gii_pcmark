# модели тестов

from django.core.exceptions import ValidationError
from django.db import models

from django_gii_pcmark.models.dicts import (
    OSDict, GPUDriversDict, TestSoftDict, TestScreenSizeDict, TestQualityDict,
    DXVersionsDict, AntiAliasingDict
)
from django_gii_pcmark.models.hardware import System


class TestPack(models.Model):
    """
    пачка тестов
    """
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    url = models.URLField()
    screen_size = models.ForeignKey(TestScreenSizeDict, on_delete=models.CASCADE, blank=True, null=True)

    os = models.ForeignKey(OSDict, on_delete=models.CASCADE, null=True, blank=True)
    gpu_driver = models.ForeignKey(GPUDriversDict, on_delete=models.CASCADE, null=True, blank=True)

    overclock_cpu_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_gpu_core_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_gpu_ram_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_ram_freq = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Тесты систем, пачки'

    def __str__(self):
        """
        строкове представление объекта
        :return:
        """
        return '{0} {1}'.format(self.system, self.screen_size)


class Mark(models.Model):
    """
    модель теста
    """

    test_pack = models.ForeignKey(TestPack, on_delete=models.CASCADE, null=True)
    system = models.ForeignKey(System, on_delete=models.CASCADE, blank=True)

    test_soft = models.ForeignKey(TestSoftDict, on_delete=models.CASCADE)
    test_soft_version = models.CharField(max_length=100, null=True, blank=True)
    test_quality = models.ForeignKey(TestQualityDict, null=True, blank=True, on_delete=models.CASCADE)
    directx_version = models.ForeignKey(DXVersionsDict, on_delete=models.CASCADE, null=True, blank=True)
    anti_aliasing_version = models.ForeignKey(AntiAliasingDict, on_delete=models.CASCADE, null=True, blank=True)
    screen_size = models.ForeignKey(TestScreenSizeDict, on_delete=models.CASCADE, blank=True, null=True)

    url = models.URLField()
    os = models.ForeignKey(OSDict, on_delete=models.CASCADE, null=True, blank=True)
    gpu_driver = models.ForeignKey(GPUDriversDict, on_delete=models.CASCADE, null=True, blank=True)

    val_min = models.PositiveIntegerField()
    val_max = models.PositiveIntegerField(null=True, blank=True)
    val_avg = models.PositiveIntegerField(null=True, blank=True)

    comments = models.TextField(null=True, blank=True)

    overclock_cpu_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_gpu_core_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_gpu_ram_freq = models.PositiveIntegerField(null=True, blank=True)
    overclock_ram_freq = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Тесты систем'

    def __str__(self):
        """
        строковое представление объекта
        :return:
        """
        return '{0} {1}'.format(self.test_pack, self.id)

    def validate_unique(self, exclude=None):
        """
        валидация на уникальность
        :param exclude:
        :return:
        """
        exists_query = Mark.objects.filter(
            system=self.system,
            test_soft=self.test_soft,
            test_quality=self.test_quality,
            screen_size=self.screen_size,
            val_min=self.val_min,
        )
        if self.id:
            exists_query = exists_query.exclude(id=self.id)

        if exists_query.exists():
            raise ValidationError('System exists')

    def save(self, *args, **kwargs):
        """
        сохранение модели
        :param args:
        :param kwargs:
        :return:
        """
        if self.system is None:
            self.system = self.test_pack.system
            self.url = self.test_pack.url
            self.screen_size = self.test_pack.screen_size
            self.os = self.test_pack.os
            self.gpu_driver = self.test_pack.gpu_driver
            self.overclock_cpu_freq = self.test_pack.overclock_cpu_freq
            self.overclock_gpu_core_freq = self.test_pack.overclock_gpu_core_freq
            self.overclock_gpu_ram_freq = self.test_pack.overclock_gpu_ram_freq
            self.overclock_ram_freq = self.test_pack.overclock_ram_freq

        super(Mark, self).save(*args, **kwargs)
