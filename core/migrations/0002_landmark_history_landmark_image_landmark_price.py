# Generated by Django 4.2.16 on 2024-10-12 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landmark',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landmark',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='landmarks/'),
        ),
        migrations.AddField(
            model_name='landmark',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
