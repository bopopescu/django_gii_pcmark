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
    # readonly_fields = (
    #     'system'
    # )




admin.site.register(Mark, MarkAdmin)
admin.site.register(TestPack, TestPackAdmin)
