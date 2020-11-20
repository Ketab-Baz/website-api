# Generated by Django 3.1.3 on 2020-11-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201120_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_critic',
        ),
        migrations.AlterField(
            model_name='user',
            name='blocked_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
