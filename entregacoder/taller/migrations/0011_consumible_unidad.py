# Generated by Django 4.2 on 2023-06-12 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taller", "0010_operario_descripcion"),
    ]

    operations = [
        migrations.AddField(
            model_name="consumible",
            name="unidad",
            field=models.CharField(default="c/u", max_length=10),
        ),
    ]
