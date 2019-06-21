"""
админка для справочников
"""

from django.contrib import admin

from django_gii_pcmark.models.dicts import (
    RamSizeDicts, SocketsDict, ProducersDict, ProcessorSeriesDict, FanSizesDict, PowersDict,
    RamSpeedRatingDict, MBPowerSchemas, DDRVersionDict, MBFormFactorDict, RamBitDict,
    OSDict, GPUDriversDict, DXVersionsDict, TestSoftDict,
    TestScreenSizeDict)


class RamSizeDictAdmin(admin.ModelAdmin):
    """
    админка для размеров памяти
    """
    ordering = ('size', 'dimension')
    list_display = ('size', 'dimension')


class SocketsDictAdmin(admin.ModelAdmin):
    """
    админка для сокетов
    """
    ordering = ('name', )
    list_display = ('name', )


class ProducersDictAdmin(admin.ModelAdmin):
    """
    админка для производителей
    """
    ordering = ('name', )
    list_display = ('name', )


class ProcessorSeriesDictAdmin(admin.ModelAdmin):
    """
    админка для серии процессора
    """
    ordering = ('name', )
    list_display = ('name', )


class FanSizesDictAdmin(admin.ModelAdmin):
    """
    админка для серии размеров вентилятора
    """
    ordering = ('size', )
    list_display = ('size', )


class PowersDictAdmin(admin.ModelAdmin):
    """
    админка для мощности
    """
    ordering = ('power', )
    list_display = ('power', )


class RamSpeedRatingDictAdmin(admin.ModelAdmin):
    """
    админка для рейтинга по частоте памяти
    """
    ordering = ('rating', )
    list_display = ('rating', 'frequence')


class MBPowerSchemasAdmin(admin.ModelAdmin):
    """
    админка для схемы питания матринских плат
    """
    ordering = ('main', 'slave')
    list_display = ('main', 'slave')


class DDRVersionDictAdmin(admin.ModelAdmin):
    """
    админка для версии ddr
    """
    ordering = ('version', )
    list_display = ('version', )


class MBFormFactorDictAdmin(admin.ModelAdmin):
    """
    админка для форм факторов материнских плат
    """
    ordering = ('form_factor', )
    list_display = ('form_factor', )


class RamBitDictAdmin(admin.ModelAdmin):
    """
    админка для битности памяти
    """
    ordering = ('bit', )
    list_display = ('bit', )


class OSDictAdmin(admin.ModelAdmin):
    """
    админка для операционных систем
    """
    ordering = ('name', )
    list_display = ('name', )


class GPUDriversDictAdmin(admin.ModelAdmin):
    """
    админка для драйверов видеокарт
    """
    ordering = ('name', 'version')
    list_display = ('name', 'version')


class TestSoftDictAdmin(admin.ModelAdmin):
    """
    админка для тестовых программ
    """
    ordering = ('name', 'mode', 'version')
    list_display = ('name', 'mode', 'version')


class DXVersionsDictAdmin(admin.ModelAdmin):
    """
    админка для версии directx
    """
    ordering = ('version', )
    list_display = ('version', )


class TestScreenSizeDictAdmin(admin.ModelAdmin):
    """
    разрешения экранов в тестах
    """
    ordering = ('width', 'height')
    list_display = ('width', 'height')


admin.site.register(RamSizeDicts, RamSizeDictAdmin)
admin.site.register(SocketsDict, SocketsDictAdmin)
admin.site.register(ProducersDict, ProducersDictAdmin)
admin.site.register(ProcessorSeriesDict, ProcessorSeriesDictAdmin)
admin.site.register(FanSizesDict, FanSizesDictAdmin)
admin.site.register(PowersDict, PowersDictAdmin)
admin.site.register(RamSpeedRatingDict, RamSpeedRatingDictAdmin)
admin.site.register(MBPowerSchemas, MBPowerSchemasAdmin)
admin.site.register(DDRVersionDict, DDRVersionDictAdmin)
admin.site.register(MBFormFactorDict, MBFormFactorDictAdmin)
admin.site.register(RamBitDict, RamBitDictAdmin)
admin.site.register(OSDict, OSDictAdmin)
admin.site.register(GPUDriversDict, GPUDriversDictAdmin)
admin.site.register(DXVersionsDict, DXVersionsDictAdmin)
admin.site.register(TestSoftDict, TestSoftDictAdmin)
admin.site.register(TestScreenSizeDict, TestScreenSizeDictAdmin)
