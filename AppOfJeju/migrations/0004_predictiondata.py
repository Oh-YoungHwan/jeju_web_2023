# Generated by Django 4.2.4 on 2023-11-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppOfJeju", "0003_cropmarketdata_origin"),
    ]

    operations = [
        migrations.CreateModel(
            name="PredictionData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("crop_type", models.CharField(max_length=20)),
                ("supplier", models.CharField(blank=True, max_length=20)),
                ("origin", models.CharField(blank=True, max_length=20)),
                ("crop_date", models.DateField()),
                ("crop_supply", models.FloatField()),
                ("crop_price", models.FloatField()),
                ("ai_model", models.CharField(max_length=30)),
            ],
        ),
    ]