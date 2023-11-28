# Generated by Django 4.2.4 on 2023-08-24 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("django_app", "0006_alter_item_track"),
    ]

    operations = [
        migrations.CreateModel(
            name="Find",
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
                (
                    "tracks",
                    models.ManyToManyField(
                        to="django_app.item", verbose_name="Трек код"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Трек код",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отслеживание",
                "verbose_name_plural": "Отслеживания",
                "ordering": ("user",),
            },
        ),
    ]
