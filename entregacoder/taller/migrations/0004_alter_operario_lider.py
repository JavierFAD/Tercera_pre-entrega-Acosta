# Generated by Django 4.2 on 2023-06-12 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("taller", "0003_alter_operario_lider"),
    ]

    operations = [
        migrations.AlterField(
            model_name="operario",
            name="lider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="operario",
                to="taller.lider",
            ),
        ),
    ]
