# Generated by Django 3.1.6 on 2021-02-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assumptions', '0017_auto_20210225_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assumptions',
            name='slug',
            field=models.CharField(default=models.IntegerField(verbose_name='No. of working hrs. per day'), max_length=25),
        ),
    ]
