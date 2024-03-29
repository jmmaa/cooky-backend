from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    number_of_servings = models.IntegerField()
    preparation_time = models.TimeField()
    image = models.ImageField(blank=True)

    ingredients = models.TextField()
    procedure = models.TextField()

    def __str__(self) -> str:
        return self.name


class UserRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}'s {self.recipe.name}"


class UserRecipeCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_recipe = models.ForeignKey(UserRecipe, on_delete=models.CASCADE)

    class Meta:  # pyright: ignore [reportIncompatibleVariableOverride]
        unique_together = ("user", "user_recipe")
