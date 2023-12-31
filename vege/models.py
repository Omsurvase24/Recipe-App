from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
    recipe_view_count = models.IntegerField(default=1)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name


class Comment(models.Model):
    post = models.ForeignKey(
        Recipe, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.recipe_name, self.name)
