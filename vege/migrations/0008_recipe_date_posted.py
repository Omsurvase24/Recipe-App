# Generated by Django 5.0 on 2023-12-16 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0007_alter_recipe_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 12, 16, 18, 54, 29, 869592, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
