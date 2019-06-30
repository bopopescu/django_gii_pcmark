# модели железок

import os
from time import time

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from django_gii_pcmark.models.dicts import (
    ProcessorSeriesDict, ProducersDict, SocketsDict, RamSizeDicts, PowersDict, FanSizesDict,
    MBPowerSchemas, DDRVersionDict, MBFormFactorDict, RamBitDict,
    RamSpeedRatingDict, LanChipsetsDict, WifiChipsetDict, WifiVersionsDict)


class CPUGpu(models.Model):
    """
    видеочипсте процессора
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    frequence_baze = models.PositiveIntegerField()

    frequence_max = models.PositiveIntegerField()

    core_count = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1} ({2}/{3})'.format(self.producer, self.model, self.frequence_baze, self.frequence_max)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Процессор, видеочипсет'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model'], name='cpu_gpu_producer_model_uniq')
        ]


class AudioCodec(models.Model):
    """
    звуковой кодек
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1}'.format(self.producer, self.model)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Аудио кодек'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model'], name='audio_producer_model_uniq')
        ]


class MBChipsets(models.Model):
    """
    чипсеты материнских плат
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1}'.format(self.producer, self.model)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Материнские платы, чипсеты'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model'], name='mb_chipset_producer_model_uniq')
        ]


class CPU(models.Model):
    """
    модель процессора
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # серия процессора, core-i3, ...
    series = models.ForeignKey(ProcessorSeriesDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    # частота
    frequency = models.PositiveIntegerField()

    # частота
    frequency_max = models.PositiveIntegerField()

    # сокет
    socket = models.ForeignKey(SocketsDict, on_delete=models.CASCADE)

    # количество ядер
    cores_count = models.PositiveSmallIntegerField()

    # количество потоков
    threads_count = models.PositiveSmallIntegerField()

    cache1_lvl = models.ForeignKey(
        RamSizeDicts,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='cache1_lvl')
    cache2_lvl = models.ForeignKey(
        RamSizeDicts,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='cache2_lvl')
    cache3_lvl = models.ForeignKey(
        RamSizeDicts,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='cache3_lvl')
    cache = models.ForeignKey(
        RamSizeDicts,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='cache')

    gpu = models.ForeignKey(CPUGpu, on_delete=models.CASCADE, null=True, blank=True)

    min_power = models.ForeignKey(
        PowersDict,
        on_delete=models.CASCADE,
        related_name='cpu_min_power',
        null=True,
        blank=True,
    )
    max_power = models.ForeignKey(
        PowersDict,
        on_delete=models.CASCADE,
        related_name='cpu_max_power',
        null=True,
        blank=True,
    )

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1} {2} ({3} | {4})'.format(
            self.producer,
            self.series,
            self.model,
            self.socket,
            self.frequency
        )


    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Процессоры'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'series', 'model'], name='cpu_producer_series_model_uniq')
        ]


class GPU(models.Model):
    """
    графический процессор
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1}'.format(self.producer, self.model)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Процессоры графические'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model'], name='gpu_producer_model_uniq')
        ]


class MotherBoard(models.Model):
    """
    материнская плата
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    # сокет
    socket = models.ForeignKey(SocketsDict, on_delete=models.CASCADE)

    # количество hdmi входов
    hdmi_count = models.PositiveSmallIntegerField(null=True, blank=True)

    # количество dvi входов
    dvi_count = models.PositiveSmallIntegerField(null=True, blank=True)

    # количество vga входов
    vga_count = models.PositiveSmallIntegerField(null=True, blank=True)

    # количество sata3 входов
    sata3_count = models.PositiveSmallIntegerField(null=True, blank=True)

    # количество m2 входов
    m2_count = models.PositiveSmallIntegerField(null=True, blank=True)

    usb2_count = models.PositiveSmallIntegerField(null=True, blank=True)

    usb3_count = models.PositiveSmallIntegerField(null=True, blank=True)

    lan_chipset = models.ForeignKey(LanChipsetsDict, on_delete=models.CASCADE, null=True, blank=True)
    lan1_speed = models.PositiveSmallIntegerField(null=True, blank=True)
    lan2_speed = models.PositiveSmallIntegerField(null=True, blank=True)

    wifi_chipset = models.ForeignKey(WifiChipsetDict, on_delete=models.CASCADE, null=True, blank=True)
    wifi_versions = models.ForeignKey(WifiVersionsDict, on_delete=models.CASCADE, null=True, blank=True)

    # количество слотов памяти
    ddr_count = models.PositiveSmallIntegerField(null=True, blank=True)

    # ddr версия
    ddr_version = models.ForeignKey(DDRVersionDict, on_delete=models.CASCADE)

    # аудиокодек
    audio_codec = models.ForeignKey(AudioCodec, on_delete=models.CASCADE)

    # питание
    power_schema = models.ForeignKey(MBPowerSchemas, on_delete=models.CASCADE)

    # чипсет
    chipset = models.ForeignKey(MBChipsets, on_delete=models.CASCADE)

    # форм фактор
    form_factor = models.ForeignKey(MBFormFactorDict, on_delete=models.CASCADE, null=True, blank=True)

    # высота
    height = models.PositiveIntegerField(null=True, blank=True)

    # ширина
    width = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1} ({2})'.format(self.producer, self.model, self.socket)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Материнские платы'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model'], name='mb_producer_model_uniq')
        ]


class VideoCard(models.Model):
    """
    видеокарта
    """

    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)

    cores = models.PositiveIntegerField()

    # память
    ram_version = models.ForeignKey(DDRVersionDict, on_delete=models.CASCADE)
    ram_bit = models.ForeignKey(RamBitDict, on_delete=models.CASCADE)
    ram_size = models.ForeignKey(RamSizeDicts, on_delete=models.CASCADE)

    ram_frequency_min = models.PositiveIntegerField(null=True, blank=True)
    ram_frequency_max = models.PositiveIntegerField(null=True, blank=True)

    ram_speed_min = models.PositiveIntegerField(null=True, blank=True)
    ram_speed_max = models.PositiveIntegerField(null=True, blank=True)

    gpu_frequency = models.PositiveIntegerField(null=True, blank=True)
    gpu_frequency_max = models.PositiveIntegerField(null=True, blank=True)

    # питание
    power_schema = models.ForeignKey(MBPowerSchemas, on_delete=models.CASCADE, null=True, blank=True)

    hdmi_count = models.PositiveSmallIntegerField(null=True, blank=True)
    vga_count = models.PositiveSmallIntegerField(null=True, blank=True)
    dvi_count = models.PositiveSmallIntegerField(null=True, blank=True)
    display_port_count = models.PositiveSmallIntegerField(null=True, blank=True)
    usb_c_count = models.PositiveSmallIntegerField(null=True, blank=True)

    height = models.PositiveSmallIntegerField('Высота', null=True, blank=True)
    width = models.PositiveIntegerField('Ширина', null=True, blank=True)
    length = models.PositiveIntegerField('Длина', null=True, blank=True)

    min_power = models.ForeignKey(
        PowersDict,
        on_delete=models.CASCADE,
        related_name='min_power',
        null=True,
        blank=True,
    )
    max_power = models.ForeignKey(
        PowersDict,
        on_delete=models.CASCADE,
        related_name='max_power',
        null=True,
        blank=True,
    )

    def __str__(self):
        """
        строкове представление объекта
        """
        return (
            '{gpu}{gpu_freq} ({ram_version} | {ram_bit} bit | {ram_size} | {freq1}{freq2}'.format(
                gpu=self.gpu,
                ram_version=self.ram_version,
                ram_bit=self.ram_bit,
                ram_size=self.ram_size,
                gpu_freq=(
                    ' {0}/{1}'.format(self.gpu_frequency or '-', self.gpu_frequency_max or '-')
                    if self.gpu_frequency or self.gpu_frequency_max
                    else ''
                ),
                freq1=(
                    ' {0}/{1}'.format(self.ram_frequency_min or '-', self.ram_speed_min or '-')
                    if self.ram_frequency_min or self.ram_speed_min
                    else ''
                ),
                freq2=(
                    ' {0}/{1}'.format(self.ram_frequency_max or '-', self.ram_speed_max or '-')
                    if self.ram_frequency_max or self.ram_speed_max
                    else ''
                ),
            )
        )

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Видеокарты'


class Ram(models.Model):
    """
    оперативная память
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    ddr_version = models.ForeignKey(DDRVersionDict, on_delete=models.CASCADE)

    size = models.ForeignKey(RamSizeDicts, on_delete=models.CASCADE)

    speed_rating = models.ForeignKey(RamSpeedRatingDict, on_delete=models.CASCADE)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1} {2}-{3}'.format(self.producer, self.model, self.ddr_version, self.size)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Оперативная память'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model', 'ddr_version', 'size'], name='ram_producer_model_ddr_version_size_uniq')
        ]


class SSD(models.Model):
    """
    ssd диски
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    # размер
    size = models.ForeignKey(RamSizeDicts, on_delete=models.CASCADE)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1} {2}'.format(self.producer, self.model, self.size)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Диски SSD'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model'], name='ssd_producer_model_uniq')
        ]


class HDD(models.Model):
    """
    hdd диски
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    # размер
    size = models.ForeignKey(RamSizeDicts, on_delete=models.CASCADE)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1} {2}'.format(self.producer, self.model, self.size)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Диски HDD'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model'], name='hdd_producer_model_uniq')
        ]


class PowerSupply(models.Model):
    """
    блок питания
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    # мощность
    power = models.ForeignKey(PowersDict, on_delete=models.CASCADE)

    # размер вентилятора
    fan_size = models.ForeignKey(FanSizesDict, on_delete=models.CASCADE)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1} {2} Ватт'.format(self.producer, self.model, self.power)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Блоки питания'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model', 'power'], name='ps_producer_model_power_uniq')
        ]


class CPUFan(models.Model):
    """
    охлаждение процессора
    """

    # производитель
    producer = models.ForeignKey(ProducersDict, on_delete=models.CASCADE)

    # модель, 8350К
    model = models.CharField(max_length=100)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1}'.format(self.producer, self.model)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Процессор, охлаждение'
        constraints = [
            models.UniqueConstraint(fields=['producer', 'model'], name='cpu_fan_producer_model_uniq')
        ]


class System(models.Model):
    """
    система
    """

    mother_board = models.ForeignKey(MotherBoard, on_delete=models.CASCADE)

    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)

    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)

    ram_count = models.PositiveSmallIntegerField()

    video_card = models.ForeignKey(VideoCard, on_delete=models.CASCADE, null=True)

    ssd = models.ForeignKey(SSD, on_delete=models.CASCADE, null=True, blank=True)

    hdd = models.ForeignKey(HDD, on_delete=models.CASCADE, null=True, blank=True)

    cpu_fan = models.ForeignKey(CPUFan, on_delete=models.CASCADE, null=True, blank=True)

    power_supply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        """
        строкове представление объекта
        """
        return '{0} {1} {2}x{3}{4}{5}{6}{7}'.format(
            self.mother_board,
            self.cpu,
            self.ram,
            self.ram_count,
            ' {}'.format(self.video_card) if self.video_card else '',
            ' {}'.format(self.ssd or self.hdd) if self.ssd or self.hdd else '',
            ' {}'.format(self.cpu_fan) if self.cpu_fan else '',
            ' {}'.format(self.power_supply) if self.power_supply else '',
        )

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Система'
        constraints = [
            models.UniqueConstraint(
                fields=['mother_board', 'cpu', 'ram', 'ram_count', 'video_card', 'ssd', 'hdd'],
                name='system_uniq'
            )
        ]


def upload_to(instance, filename):
    """
    вычисляем путь загрузки файла
    """

    return os.path.join(
        'django_gii_pcmark',
        instance.content_object.__class__.__name__.lower(),
        '{0}_{1}{2}'.format(instance.object_id, int(time()), os.path.splitext(filename)[-1])
    )


class FilesCT(models.Model):
    """
    файлы железок
    """
    file = models.FileField(upload_to=upload_to)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")