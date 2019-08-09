from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Recipe(models.Model):
    name = models.TextField(null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def steps(self):
        return self.step_set.all()

    @property
    def ingredients(self):
        return self.ingredient_set.all()


class Step(models.Model):
    step_text = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.step_text


class Ingredient(models.Model):
    text = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
