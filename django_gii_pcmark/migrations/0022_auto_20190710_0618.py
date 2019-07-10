# Generated by Django 2.2 on 2019-07-10 03:18

from django.db import migrations


def move_test_to_test_pack(apps, schema):
    """

    :param apps:
    :param schema:
    :return:
    """
    Mark = apps.get_model('django_gii_pcmark', 'Mark')
    TestPack = apps.get_model('django_gii_pcmark', 'TestPack')

    for mark in Mark.objects.all():
        test_pack, _ = TestPack.objects.get_or_create(system=mark.system)
        mark.test_pack = test_pack
        mark.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0021_auto_20190709_2137'),
    ]

    operations = [
        migrations.RunPython(move_test_to_test_pack)
    ]