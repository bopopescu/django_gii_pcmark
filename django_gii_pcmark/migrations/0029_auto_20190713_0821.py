# Generated by Django 2.2 on 2019-07-13 05:21

from django.db import migrations


def move_test_to_test_pack(apps, schema):
    """

    :param apps:
    :param schema:
    :return:
    """
    Mark = apps.get_model('django_gii_pcmark', 'Mark')

    for mark in Mark.objects.all():
        mark.system = mark.test_pack.system
        mark.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0028_mark_system'),
    ]

    operations = [
        migrations.RunPython(move_test_to_test_pack)
    ]
