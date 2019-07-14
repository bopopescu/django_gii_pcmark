# справчоники

from django.db import models


class SimpleNameDict(models.Model):
    """
    простой справочник имен
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return self.name

    class Meta:
        """
        мета описание модели
        """
        abstract = True


class ProcessorSeriesDict(SimpleNameDict):
    """
    серия процессора
    core-i3, etc
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: процессор серия'


class ProducersDict(SimpleNameDict):
    """
    производители
    intel, etc
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: производители'


class SocketsDict(SimpleNameDict):
    """
    сокеты
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: процессор сокет'


class OSDict(SimpleNameDict):
    """
    справочник операционных систем
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: операционные системы'


class LanChipsetsDict(SimpleNameDict):
    """
    справочник чипсетов сетевых карт
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: чипсеты сетевых карт'


class WifiChipsetDict(SimpleNameDict):
    """
    справочник чипсетов вай фай карт
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: чипсеты wi-fi карт'


class WifiVersionsDict(SimpleNameDict):
    """
    справочник версии вай фай карт
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: версии wi-fi карт'


class TestQualityDict(SimpleNameDict):
    """
    справочник настроек теста
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: тест режим настроек'


class DXVersionsDict(SimpleNameDict):
    """
    справочник версии DX
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: тест версии DX'


class AntiAliasingDict(SimpleNameDict):
    """
    справочник версии AA
    """

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: тест версии AA'


class RamSizeDicts(models.Model):
    """
    размеры памяти
    """

    # количество
    size = models.PositiveIntegerField()

    # размерность
    dimension = models.CharField(max_length=100)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1}'.format(self.size, self.dimension)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: память размеры'
        constraints = [
            models.UniqueConstraint(fields=['size', 'dimension'], name='size_dimension_uniq')
        ]


class PowersDict(models.Model):
    """
    мощность
    """

    power = models.PositiveIntegerField(unique=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return str(self.power)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: мощности'


class FanSizesDict(models.Model):
    """
    размеры вентиляторов
    """

    size = models.PositiveIntegerField(unique=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return str(self.size)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: охлаждение, размеры вентилятора'


class MBPowerSchemas(models.Model):
    """
    схемы питания материнских плат
    """

    main = models.PositiveSmallIntegerField()
    slave = models.PositiveSmallIntegerField()

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} x {1}'.format(self.main, self.slave)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: схема питания материнских плат'


class DDRVersionDict(models.Model):
    """
    версии ddr
    """

    version = models.CharField(max_length=10, unique=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return self.version

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: версии ddr'


class MBFormFactorDict(models.Model):
    """
    форм факторы материнских плат
    """

    form_factor = models.CharField(max_length=10, unique=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return self.form_factor

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: материнская плата, форм фактор'


class RamBitDict(models.Model):
    """
    битность памяти
    """

    bit = models.PositiveIntegerField(unique=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return str(self.bit)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: память, битность'


class RamSpeedRatingDict(models.Model):
    """
    память PC4-24000 (3000)
    """

    rating = models.CharField(max_length=20)

    frequence = models.PositiveIntegerField()

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} ({1} MHz)'.format(self.rating, self.frequence)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: память, рейтинг по частоте'


class GPUDriversDict(models.Model):
    """
    справочник драйверов видеокард
    """

    name = models.CharField(max_length=100)

    version = models.CharField(max_length=100)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1}'.format(self.name, self.version)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: драйвер видеокарты'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'version'],
                name='gpu_driver_name_version_uniq'
            )
        ]


class TestSoftDict(models.Model):
    """
    тестовая программа
    """

    name = models.CharField(max_length=100)

    mode = models.CharField(max_length=100, null=True, blank=True)

    dimension = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0}{1}{2}'.format(
            self.name,
            ' {0}'.format(self.mode) if self.mode else '',
            ' {0}'.format(self.dimension) if self.dimension else ''
        )

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: тестовая программа'


class TestScreenSizeDict(models.Model):
    """
    разрешение экрана в тестах
    """

    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0}x{1}'.format(self.width, self.height)

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: тестовые разрешения экранов'
        constraints = [
            models.UniqueConstraint(
                fields=['width', 'height'],
                name='test_screen_size_width_height_uniq'
            )
        ]
