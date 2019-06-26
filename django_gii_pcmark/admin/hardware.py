"""
админка для железа
"""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from django_gii_pcmark.admin.marks import MarkAdmin
from django_gii_pcmark.models.hardware import (
    CPU, MotherBoard, VideoCard, Ram, SSD, HDD, PowerSupply, System, FilesCT, AudioCodec,
    MBChipsets, GPU, CPUGpu, CPUFan,
)
from django_gii_pcmark.models.marks import Mark


class FileInline(GenericTabularInline):
    """
    файлы железок
    """
    model = FilesCT


class TestInline(admin.StackedInline):
    """
    тесты систем
    """
    model = Mark
    extra = 1

    fieldsets = MarkAdmin.fieldsets


class CPUAdmin(admin.ModelAdmin):
    """
    админка для процессоров
    """
    ordering = ('producer', 'series', 'model')
    list_display = ('producer', 'series', 'model', 'frequency', 'socket')
    fieldsets = (
        (
            'Модель',
            {
                'fields': (('producer', 'series', 'model'), 'socket', 'official_url')
            }
        ),
        (
            'Характеристики',
            {
                'fields': (
                    ('cores_count', 'threads_count'),
                    ('frequency', 'frequency_max'),
                    ('cache', 'cache1_lvl', 'cache2_lvl', 'cache3_lvl'),
                    'gpu',
                )
            }
        )
    )

    inlines = [
        FileInline
    ]


class MotherBoardAdmin(admin.ModelAdmin):
    """
    админка для материнских плат
    """
    list_display = ('producer', 'model', 'socket')
    fieldsets = (
        (
            'Модель',
            {
                'fields': (('producer', 'model', 'form_factor'), ('height', 'width'), 'official_url')
            }
        ),
        (
            'Чипы и питание',
            {
                'fields': (('socket', 'power_schema'), ('chipset', 'audio_codec'))
            }
        ),
        (
            'ОЗУ',
            {
                'fields': (('ddr_version', 'ddr_count'), )
            }
        ),
        (
            'Перифирия',
            {
                'fields': (('hdmi_count', 'dvi_count', 'vga_count'), ('sata3_count', 'm2_count'), )
            }
        ),
    )
    inlines = [
        FileInline
    ]


class VideoCardAdmin(admin.ModelAdmin):
    """
    админка для видеокарт
    """
    ordering = ('producer', 'model', 'gpu')
    list_display = ('producer', 'model', 'gpu')
    fieldsets = (
        (
            'Модель',
            {
                'fields': (
                    ('producer', 'model', 'gpu', 'gpu_frequency', 'gpu_frequency_max'),
                    'official_url',
                )
            }
        ),
        (
            'Память',
            {
                'fields': (
                    ('ram_version', 'ram_size', 'ram_bit', 'ram_frequency'),
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
    list_display = ('producer', 'model', 'ddr_version', 'speed_rating')

    fieldsets = (
        (
            'Модель',
            {
                'fields': (
                    ('producer', 'model'),
                    'official_url',
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


class SystemAdmin(admin.ModelAdmin):
    """
    админка для системы
    """
    list_filter = ('mother_board', 'cpu')
    list_display = ('mother_board', 'cpu', 'ram', 'ram_count', 'video_card', 'ssd', 'hdd', 'cpu_fan')
    fields = (

        ('mother_board', 'cpu', 'video_card'),
        ('ram', 'ram_count'),
        ('ssd', 'hdd'),
        ('cpu_fan', 'power_supply'),
    )
    inlines = [
        TestInline
    ]


class FilesCTAdmin(admin.ModelAdmin):
    """
    админка для файлов
    """
    list_display = ('file', 'content_type', 'object_id')


class AudioCodecAdmin(admin.ModelAdmin):
    """
    админка для аудио кодеков
    """
    list_display = ('producer', 'model')


class MBChipsetsAdmin(admin.ModelAdmin):
    """
    админка для чипсетов материнских плат
    """
    list_display = ('producer', 'model')


class GPUAdmin(admin.ModelAdmin):
    """
    админка для видеокартных процессоров 
    """
    list_display = ('producer', 'model', 'cores')


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
admin.site.register(GPU, GPUAdmin)
admin.site.register(CPUFan, CPUFanAdmin)
admin.site.register(CPUGpu, CPUGpuAdmin)
