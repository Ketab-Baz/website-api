# Generated by Django 3.1.3 on 2020-12-31 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201231_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critic',
            name='blocked_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='critic',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
