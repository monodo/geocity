# Generated by Django 2.1.2 on 2018-12-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0006_auto_20181204_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permitrequest',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='permitrequest',
            name='date_end_work',
            field=models.DateField(blank=True, null=True, verbose_name='date_end_work'),
        ),
        migrations.AlterField(
            model_name='permitrequest',
            name='date_end_work_announcement',
            field=models.DateField(blank=True, null=True, verbose_name='date_end_work_announcement'),
        ),
    ]
