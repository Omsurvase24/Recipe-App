# Generated by Django 5.0 on 2023-12-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_recipe_created_at_recipe_no_of_likes_alter_recipe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='no_of_likes',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
