# Generated by Django 4.2.5 on 2023-10-04 03:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="-"),
        ),
    ]
