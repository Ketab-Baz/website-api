# Generated by Django 3.1.3 on 2020-12-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201120_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='blocked_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
