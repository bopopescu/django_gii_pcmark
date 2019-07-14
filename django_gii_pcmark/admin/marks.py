"""
админка для тестов
"""

from django.contrib import admin

from django_gii_pcmark.models.dicts import ProducersDict
from django_gii_pcmark.models.marks import Mark, TestPack


class VideoCardProducerFilter(admin.SimpleListFilter):
    """
    фильтр по производителям
    """
    title = 'производитель'
    parameter_name = 'vc_producer'

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
            return queryset.filter(system__video_card__producer=value)


class MarkAdmin(admin.ModelAdmin):
    """
    админка для теста
    """
    save_as = True

    fieldsets = (
        (
            'Стенд и окружение',
            {
                'fields': (
                    'system',
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
    list_filter = (
        VideoCardProducerFilter,
        'system__mother_board',
        'system__cpu__series',
        'test_soft__name',
    )


class MarkInline(admin.StackedInline):
    """
    тесты систем
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
        'system__video_card__producer__name',
        'system__video_card__model',
        'system__gpu_producer__name',
        'system__gpu_model',
        'screen_size__width',
        'screen_size__height',
    )

admin.site.register(Mark, MarkAdmin)
admin.site.register(TestPack, TestPackAdmin)
