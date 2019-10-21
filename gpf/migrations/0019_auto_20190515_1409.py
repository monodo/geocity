# Generated by Django 2.2 on 2019-05-15 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0018_department_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArcheoStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='archeo_status')),
            ],
            options={
                'verbose_name': 'archeostatus',
            },
        ),
        migrations.AlterField(
            model_name='permitrequest',
            name='has_archeology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gpf.ArcheoStatus', verbose_name='archeostatus'),
        ),
    ]
