# Generated by Django 3.2.21 on 2023-12-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainTableInput', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
    ]
