# Generated by Django 3.1.6 on 2021-02-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assumptions', '0002_absenteeis_and_defective_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absenteeis_and_defective',
            name='Defective_Goods',
            field=models.CharField(choices=[('year1', 'year1'), ('year2', 'year2'), ('year3', 'year3')], default=None, max_length=25),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
