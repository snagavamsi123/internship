# Generated by Django 3.1.6 on 2021-03-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assumptions', '0024_auto_20210301_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assumptions',
            name='Attendance_Time_hrs_perday',
            field=models.IntegerField(null=True, verbose_name='Attendance Time (hrs per day)'),
        ),
    ]
