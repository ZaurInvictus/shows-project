# Generated by Django 3.0.5 on 2020-12-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20201225_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='Description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='description'),
        ),
    ]
