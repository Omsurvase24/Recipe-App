# Generated by Django 5.0 on 2023-12-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0016_alter_recipe_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=100),
        ),
    ]
