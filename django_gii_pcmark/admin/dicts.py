"""
админка для справочников
"""

from django.contrib import admin

from django_gii_pcmark.models.dicts import (
    RamSizeDicts, SocketsDict, ProducersDict, ProcessorSeriesDict, FanSizesDict, PowersDict,
    RamSpeedRatingDict, MBPowerSchemas, DDRVersionDict, MBFormFactorDict, RamBitDict,
    OSDict, GPUDriversDict, DXVersionsDict, TestSoftDict,
    TestScreenSizeDict, LanChipsetsDict, WifiChipsetDict, WifiVersionsDict
)


class SimpleNameAdmin(admin.ModelAdmin):
    """
    админка для простых именованных справочников
    """
    ordering = ('name', )


class RamSizeDictAdmin(admin.ModelAdmin):
    """
    админка для размеров памяти
    """
    ordering = ('size', 'dimension')
    list_display = ('size', 'dimension')


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
    ordering = ('name', 'mode')
    list_display = ('name', 'mode')


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
admin.site.register(SocketsDict, SimpleNameAdmin)
admin.site.register(ProducersDict, SimpleNameAdmin)
admin.site.register(ProcessorSeriesDict, SimpleNameAdmin)
admin.site.register(FanSizesDict, FanSizesDictAdmin)
admin.site.register(PowersDict, PowersDictAdmin)
admin.site.register(RamSpeedRatingDict, RamSpeedRatingDictAdmin)
admin.site.register(MBPowerSchemas, MBPowerSchemasAdmin)
admin.site.register(DDRVersionDict, DDRVersionDictAdmin)
admin.site.register(MBFormFactorDict, MBFormFactorDictAdmin)
admin.site.register(RamBitDict, RamBitDictAdmin)
admin.site.register(OSDict, SimpleNameAdmin)
admin.site.register(GPUDriversDict, GPUDriversDictAdmin)
admin.site.register(DXVersionsDict, DXVersionsDictAdmin)
admin.site.register(TestSoftDict, TestSoftDictAdmin)
admin.site.register(TestScreenSizeDict, TestScreenSizeDictAdmin)
admin.site.register(LanChipsetsDict, SimpleNameAdmin)
admin.site.register(WifiVersionsDict, SimpleNameAdmin)
admin.site.register(WifiChipsetDict, SimpleNameAdmin)
