# Generated by Django 3.1.3 on 2020-12-31 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre_and_votes',
            field=models.CharField(max_length=2000),
        ),
    ]