"""
админка для железа
"""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from django_gii_pcmark.models.dicts import ProducersDict
from django_gii_pcmark.models.hardware import (
    CPU, MotherBoard, VideoCard, Ram, SSD, HDD, PowerSupply, System, FilesCT, AudioCodec,
    MBChipsets, CPUGpu, CPUFan,
)
from django_gii_pcmark.models.marks import Mark


class FileInline(GenericTabularInline):
    """
    файлы железок
    """
    model = FilesCT


class CPUAdmin(admin.ModelAdmin):
    """
    админка для процессоров
    """
    ordering = ('producer__name', 'series__name', 'model')
    fieldsets = (
        (
            'Модель',
            {
                'fields': (
                    ('producer', 'series', 'model', 'produce_date'),
                    ('socket', 'gpu',)
                )
            }
        ),
        (
            'Характеристики',
            {
                'fields': (
                    ('cores_count', 'threads_count'),
                    ('frequency', 'frequency_max'),
                    ('cache', 'cache1_lvl', 'cache2_lvl', 'cache3_lvl'),
                    ('min_power', 'max_power',)
                )
            }
        )
    )


class MotherBoardAdmin(admin.ModelAdmin):
    """
    админка для материнских плат
    """
    ordering = ('producer__name', 'model')
    fieldsets = (
        (
            'Модель',
            {
                'fields': (
                    ('producer', 'model', 'form_factor'),
                    ('produce_date', 'height', 'width'),
                )
            }
        ),
        (
            'Чипы и питание',
            {
                'fields': (
                    ('socket', 'power_schema'),
                    ('chipset', 'audio_codec'),
                    ('lan_chipset', 'lan1_speed', 'lan2_speed'),
                    ('wifi_chipset', 'wifi_versions'),
                )
            }
        ),
        (
            'ОЗУ',
            {
                'fields': (
                    ('ddr_version', 'ddr_count'),
                )
            }
        ),
        (
            'Перифирия',
            {
                'fields': (
                    ('hdmi_count', 'dvi_count', 'vga_count'),
                    ('sata3_count', 'm2_count'),
                    ('usb2_count', 'usb3_count'),
                )
            }
        ),
    )


class VideoCardProducerFilter(admin.SimpleListFilter):
    """
    фильтр по производителям
    """
    title = 'производитель'
    parameter_name = 'producer'

    def lookups(self, request, model_admin):
        """
        возвращаем варианты для клиента
        :param request:
        :param model_admin:
        :return:
        """
        return [
            (producer.id, str(producer.name))
            for producer in ProducersDict.objects.filter(name__in=('AMD', 'Nvidia')).order_by('name')
        ]

    def queryset(self, request, queryset):
        """
        фильтруем элементы списка
        :param request:
        :param queryset:
        :return:
        """
        value = self.value()
        if value:
            return queryset.filter(producer=value)


class VideoCardAdmin(admin.ModelAdmin):
    """
    админка для видеокарт
    """
    save_as = True
    ordering = ('producer__name', 'model', 'ram_size')
    list_filter = (VideoCardProducerFilter,)
    list_display = ('__str__', 'produce_date')
    fieldsets = (
        (
            'Процессор',
            {
                'fields': (
                    ('producer', 'model', 'cores', 'produce_date'),
                    ('gpu_frequency', 'gpu_frequency_max'),
                )
            }
        ),
        (
            'Память',
            {
                'fields': (
                    ('ram_version', 'ram_size', 'ram_bit'),
                    ('ram_frequency_min', 'ram_speed_min', 'ram_frequency_max', 'ram_speed_max'),
                )
            }
        ),
        (
            'Остальное',
            {
                'fields': (
                    ('hdmi_count', 'dvi_count', 'vga_count', 'display_port_count', 'usb_c_count'),
                    ('height', 'width', 'length'),
                    ('power_schema', 'min_power', 'max_power'),
                )
            }
        ),
    )


class RamAdmin(admin.ModelAdmin):
    """
    админка для оперативной памяти
    """
    ordering = ('producer__name', 'ddr_version__version', 'speed_rating', 'model')

    fieldsets = (
        (
            'Модель',
            {
                'fields': (
                    ('producer', 'model', 'produce_date'),
                )
            }
        ),
        (
            'Параметры',
            {
                'fields': (
                    ('ddr_version', 'size', 'speed_rating'),
                )
            }
        ),
    )


class SSDAdmin(admin.ModelAdmin):
    """
    админка для диска ssd
    """
    list_display = ('producer', 'model', 'size')


class HDDAdmin(admin.ModelAdmin):
    """
    админка для диска hdd
    """
    list_display = ('producer', 'model', 'size')


class PowerSupplyAdmin(admin.ModelAdmin):
    """
    админка для блоков памяти
    """
    list_display = ('producer', 'model', 'power')


class MarkInline(admin.StackedInline):
    """
    тесты систем
    """
    model = Mark
    fieldsets = (
        (
            'Стенд и окружение',
            {
                'fields': (
                    ('test_soft', 'test_soft_version'),
                    ('test_quality', 'anti_aliasing_version', 'directx_version'),
                    ('screen_size', 'url', 'os', 'gpu_driver'),
                    (
                        'overclock_cpu_freq',
                        'overclock_ram_freq',
                        'overclock_gpu_core_freq',
                        'overclock_gpu_ram_freq',
                    ),
                    'comments',
                ),
            }
        ),
        (
            'Показатели',
            {
                'fields': (
                    ('val_min', 'val_avg', 'val_max'),
                )
            }
        ),
    )
    ordering = (
        'test_soft__name',
        'test_soft__mode',
        'test_soft__dimension',
        'test_quality__name',
        'screen_size__width',
    )


class SystemAdmin(admin.ModelAdmin):
    """
    админка для системы
    """
    save_as = True
    save_on_top = True
    list_filter = ('mother_board', 'cpu', 'video_card__model')
    ordering = (
        'mother_board__producer__name',
        'mother_board__model',
        'cpu__producer__name',
        'cpu__series__name',
        'cpu__model',
        'video_card__producer__name',
        'video_card__model',
        'gpu_producer__name',
        'gpu_model',
    )
    fields = (
        ('mother_board', 'cpu'),
        ('video_card', 'gpu_producer', 'gpu_model'),
        ('ram', 'ram_count'),
        ('ssd', 'hdd'),
        ('cpu_fan', 'power_supply'),
        'produce_date'
    )
    inlines = [
        MarkInline
    ]
    search_fields = (
        'cpu__model',
        'video_card__model',
    )


class FilesCTAdmin(admin.ModelAdmin):
    """
    админка для файлов
    """
    list_display = ('file', 'content_type', 'object_id')


class AudioCodecAdmin(admin.ModelAdmin):
    """
    админка для аудио кодеков
    """
    ordering = ('producer__name', 'model')


class MBChipsetsAdmin(admin.ModelAdmin):
    """
    админка для чипсетов материнских плат
    """
    list_display = ('producer', 'model')


class CPUFanAdmin(admin.ModelAdmin):
    """
    админка для процессорных кулеров
    """
    list_display = ('producer', 'model')


class CPUGpuAdmin(admin.ModelAdmin):
    """
    админка для процессорных видеочипсетов
    """
    list_display = ('producer', 'model', 'frequence_baze', 'frequence_max', 'core_count')


admin.site.register(CPU, CPUAdmin)
admin.site.register(MotherBoard, MotherBoardAdmin)
admin.site.register(VideoCard, VideoCardAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(SSD, SSDAdmin)
admin.site.register(HDD, HDDAdmin)
admin.site.register(PowerSupply, PowerSupplyAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(FilesCT, FilesCTAdmin)
admin.site.register(AudioCodec, AudioCodecAdmin)
admin.site.register(MBChipsets, MBChipsetsAdmin)
admin.site.register(CPUFan, CPUFanAdmin)
admin.site.register(CPUGpu, CPUGpuAdmin)
