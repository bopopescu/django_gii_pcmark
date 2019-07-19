"""
настройка админки по тест пакам
"""

from django.contrib import admin
from django.db import connection

from django_gii_pcmark.admin.filters import MarkVideoCardFilter, MarkCPUFilter, MarkMBFilter
from django_gii_pcmark.models.hardware import CPU, VideoCard, MotherBoard
from django_gii_pcmark.models.marks import Mark, TestPack


class MarkInline(admin.StackedInline):
    """
    инлайн тесты систем
    """
    model = Mark
    extra = 15
    fieldsets = (
        (
            'Стенд и окружение',
            {
                'fields': (
                    ('test_soft', 'test_soft_version'),
                    ('test_quality', 'anti_aliasing_version', 'directx_version'),
                    'screen_size',
                    'comments',
                )
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


@admin.register(TestPack)
class TestPackAdmin(admin.ModelAdmin):
    """
    админка для пачки тестов
    """
    save_as = True
    save_on_top = True
    fieldsets = (
        (
            'Система',
            {
                'fields': (
                    'system',
                )
            }
        ),
        (
            'Окружение',
            {
                'fields': (
                    ('url', 'screen_size'),
                    ('os', 'gpu_driver'),
                    (
                        'overclock_cpu_freq',
                        'overclock_ram_freq',
                        'overclock_gpu_core_freq',
                        'overclock_gpu_ram_freq',
                    )
                )
            }
        ),
    )
    list_filter = (
        MarkMBFilter,
        MarkCPUFilter,
        MarkVideoCardFilter,
    )
    ordering = (
        'system__mother_board__producer__name',
        'system__mother_board__model',
        'system__cpu__producer__name',
        'system__cpu__series__name',
        'system__cpu__model',
        'system__video_card__producer__name',
        'system__video_card__model',
        'system__gpu_producer__name',
        'system__gpu_model',
        'screen_size__width',
        'screen_size__height',
    )
    inlines = [
        MarkInline
    ]
