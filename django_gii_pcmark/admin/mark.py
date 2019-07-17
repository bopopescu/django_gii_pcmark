"""
админка для тестов
"""

from django.contrib import admin

from django_gii_pcmark.models.dicts import ProducersDict
from django_gii_pcmark.models.marks import Mark


class VideoCardProducerFilter(admin.SimpleListFilter):
    """
    фильтр по производителям видеокард
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


@admin.register(Mark)
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
