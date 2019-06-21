# справчоники

from django.db import models


class ProcessorSeriesDict(models.Model):
    """
    серия процессора
    core-i3, etc
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
        verbose_name_plural = 'Справочник: процессор серия'


class ProducersDict(models.Model):
    """
    производители
    intel, etc
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
        verbose_name_plural = 'Справочник: производители'


class SocketsDict(models.Model):
    """
    сокеты
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
        verbose_name_plural = 'Справочник: процессор сокет'


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


class OSDict(models.Model):
    """
    справочник операционных систем
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
        verbose_name_plural = 'Справочник: операционные системы'


class DXVersionsDict(models.Model):
    """
    справочник версии dx
    """

    version = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return self.version

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: версии directx'


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

    version = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """
        строковое представление объекта
        """
        return '{0} {1}{2}'.format(
            self.name,
            self.version,
            ' {}'.format(self.mode) if self.mode else ''
        )

    class Meta:
        """
        мета описание модели
        """
        verbose_name_plural = 'Справочник: тестовая программа'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'mode', 'version'],
                name='test_soft_name_mode_version_uniq'
            )
        ]


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
