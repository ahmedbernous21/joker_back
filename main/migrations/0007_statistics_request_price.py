# Generated by Django 4.2.6 on 2024-08-21 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_user_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Statistics",
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
                ("start_date", models.DateField(default=django.utils.timezone.now)),
                ("finish_date", models.DateField(default=django.utils.timezone.now)),
                ("total_requests", models.PositiveIntegerField(default=0)),
                ("new_requests", models.PositiveIntegerField(default=0)),
                ("unseen_requests", models.PositiveIntegerField(default=0)),
                ("in_progress_requests", models.PositiveIntegerField(default=0)),
                ("finished_requests", models.PositiveIntegerField(default=0)),
                ("delivered_requests", models.PositiveIntegerField(default=0)),
                ("conversion_rate", models.FloatField(default=0.0)),
                ("average_request_time", models.DurationField(blank=True, null=True)),
                ("total_revenue", models.PositiveIntegerField(default=0)),
                ("repetitions_count", models.PositiveIntegerField(default=0)),
                ("top_article", models.CharField(default="", max_length=255)),
                ("average_size_distribution", models.JSONField(default=dict)),
                ("top_color", models.CharField(default="", max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="request",
            name="price",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
