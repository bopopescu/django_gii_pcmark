"""
админка для тестов
"""

from django.contrib import admin
from django.db import connection

from django_gii_pcmark.admin.filters import MarkVideoCardFilter, MarkMBFilter, MarkCPUFilter
from django_gii_pcmark.models.marks import Mark



class DuplicateValuesFilter(admin.SimpleListFilter):
    """
    фильтр по одинаковым значениям
    """
    title = 'одинаковые значения'
    parameter_name = 'df'

    def lookups(self, request, model_admin):
        """
        возвращаем варианты для клиента
        :param request:
        :param model_admin:
        :return:
        """
        return (('1', 'одинаковые'), )

    def queryset(self, request, queryset):
        """
        фильтруем элементы списка
        :param request:
        :param queryset:
        :return:
        """
        value = self.value()
        if not value:
            return queryset

        with connection.cursor() as cursor:
            cursor.execute(
                '''
                select
                  array_agg(distinct t_mark.id) mark_ids 
                from 
                  django_gii_pcmark_mark t_mark
                  
                  inner join
                    django_gii_pcmark_mark t_mark2
                      on
                        t_mark.id <> t_mark2.id
                        and t_mark.system_id = t_mark2.system_id
                        and t_mark.test_soft_id = t_mark2.test_soft_id
                        and 
                        (
                          (                                
                            t_mark.val_min is not null
                            and t_mark2.val_min is not null
                            and t_mark.val_avg is null
                            and t_mark2.val_avg is null
                            and t_mark.val_max is null
                            and t_mark2.val_max is null
                            and t_mark.val_min = t_mark2.val_min
                          )
                          or 
                          (
                            t_mark.val_min is not null
                            and t_mark2.val_min is not null
                            and t_mark.val_avg is not null
                            and t_mark2.val_avg is not null
                            and t_mark.val_max is null
                            and t_mark2.val_max is null
                            and t_mark.val_min = t_mark2.val_min
                            and t_mark.val_avg = t_mark2.val_avg
                          )
                          or 
                          (
                            t_mark.val_min is not null
                            and t_mark2.val_min is not null
                            and t_mark.val_avg is not null
                            and t_mark2.val_avg is not null
                            and t_mark.val_max is not null
                            and t_mark2.val_max is not null
                            and t_mark.val_min = t_mark2.val_min
                            and t_mark.val_avg = t_mark2.val_avg
                            and t_mark.val_max = t_mark2.val_max
                          )
                        )
                where 
                  t_mark.system_id in (                    
                    select
                      t_system.id
                    from
                      django_gii_pcmark_system t_system
                    where 
                      (
                        %(mb)s::int[] is null
                        or t_system.mother_board_id = any(%(mb)s::int[])
                      )
                      and
                      (
                        %(cpu)s::int[] is null
                        or t_system.cpu_id = any(%(cpu)s::int[])
                      )  
                      and
                      (
                        %(vc)s::int[] is null
                        or t_system.video_card_id = any(%(vc)s::int[])
                      )                          
                  )                    
                ''',
                {
                    'mb': '{{{0}}}'.format(','.join(request.GET.get('mb'))) if request.GET.get('mb') else None,
                    'cpu': '{{{0}}}'.format(','.join(request.GET.get('cpu'))) if request.GET.get('cpu') else None,
                    'vc': '{{{0}}}'.format(','.join(request.GET.get('vc'))) if request.GET.get('vc') else None,
                }
            )
            data = cursor.fetchall()
            try:
                mark_ids = data[0][0]
            except IndexError:
                mark_ids = None

        if mark_ids:
            queryset = queryset.filter(id__in=mark_ids)
        return queryset


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
        DuplicateValuesFilter,
        MarkMBFilter,
        MarkCPUFilter,
        MarkVideoCardFilter,
    )
    list_display = (
        'mark_system',
        'test_soft',
        'values',
        'screen_size',
    )
    ordering = (
        'test_soft__name',
        'val_avg',
        'val_min',
        'val_max',
    )
    readonly_fields = (
        'mark_system',
    )

    def mark_system(self, mark):
        """
        возвращаем строкое представление системы
        :param mark: тест
        :type mark: Mark
        :rtype: str
        """
        return (
            '{cpu.series} {cpu.model} | {vc.model} | {ram.size} x {ram_count}'.format(
                cpu=mark.system.cpu,
                vc=mark.system.video_card,
                ram=mark.system.ram,
                ram_count=mark.system.ram_count,
            )
        )

    def values(self, mark):
        """
        возвращаем строкое представление полученных значений в тесте
        :param mark: тест
        :type mark: Mark
        :rtype: str
        """
        return '{} | {} | {}'.format(
            mark.val_min or '-',
            mark.val_avg or '-',
            mark.val_max or '-',
        )
