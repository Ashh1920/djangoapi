# Generated by Django 4.0 on 2022-02-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.CharField(max_length=100),
        ),
    ]
