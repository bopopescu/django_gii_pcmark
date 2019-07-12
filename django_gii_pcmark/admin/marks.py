"""
админка для тестов
"""

from django.contrib import admin

from django_gii_pcmark.models.marks import Mark, TestPack


class MarkAdmin(admin.ModelAdmin):
    """
    админка для теста
    """

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


class MarkInline(admin.StackedInline):
    """
    тесты систем
    """
    model = Mark
    extra = 15
    fieldsets = MarkAdmin.fieldsets


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
    list_filter = ('system__mother_board', 'system__cpu', 'system__video_card')
    inlines = [
        MarkInline
    ]
    ordering = (
        'system__mother_board__producer__name',
        'system__mother_board__model',
        'system__cpu__producer__name',
        'system__cpu__series__name',
        'system__cpu__model',
        'system__video_card__gpu__producer__name',
        'system__video_card__gpu__model',
        'system__gpu_producer__name',
        'system__gpu_model',
        'screen_size__width',
        'screen_size__height',
    )
    # readonly_fields = (
    #     'system'
    # )




admin.site.register(Mark, MarkAdmin)
admin.site.register(TestPack, TestPackAdmin)
