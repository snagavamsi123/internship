# Generated by Django 3.1.6 on 2021-03-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assumptions', '0026_auto_20210301_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assumptions',
            name='No_of_working_hrs_per_day',
            field=models.IntegerField(default=0, null=True, verbose_name='No. of working hrs. per day'),
        ),
    ]
