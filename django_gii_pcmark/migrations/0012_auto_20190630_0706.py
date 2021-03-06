# Generated by Django 2.2 on 2019-06-30 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_gii_pcmark', '0011_auto_20190629_0813'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='videocard',
            name='vc_producer_model_gpu_ram_version_ram_size_uniq',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='cores',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='ram_bit',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='ram_frequency_max',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='ram_frequency_min',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='ram_size',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='ram_speed_max',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='ram_speed_min',
        ),
        migrations.RemoveField(
            model_name='gpu',
            name='ram_version',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='official_url',
        ),
        migrations.AddField(
            model_name='videocard',
            name='cores',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videocard',
            name='ram_bit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_gii_pcmark.RamBitDict'),
        ),
        migrations.AlterField(
            model_name='videocard',
            name='ram_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_gii_pcmark.RamSizeDicts'),
        ),
        migrations.AlterField(
            model_name='videocard',
            name='ram_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_gii_pcmark.DDRVersionDict'),
        ),
    ]
