# Generated by Django 5.0 on 2023-12-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_remove_recipe_created_at_remove_recipe_no_of_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='curr_user',
            field=models.CharField(default='Om', max_length=100),
        ),
    ]
