# Generated by Django 3.2.9 on 2021-11-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20211110_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchjob',
            name='submitted_at',
            field=models.DateTimeField(max_length=30),
        ),
    ]
