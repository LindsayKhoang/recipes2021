from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False, default="")
    summary = models.CharField(
        max_length=200, null=True, blank=False, default=""
    )
    content = models.TextField(null=True, blank=False, default="")
    image = models.ImageField(upload_to='uploads', null=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name_singular = models.CharField(
        max_length=200, null=True, blank=False, default=""
    )
    name_plural = models.CharField(
        max_length=200, null=True, blank=False, default=""
    )

    def __str__(self):
        return f"{self.name_singular} ({self.name_plural})"


class Unit(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False, default="")

    def __str__(self):
        return self.name


class RecipeIngredientUnit(models.Model):
    recipe = models.ForeignKey(
        Recipe, related_name="ingredients", on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=False, default=1.0)
    display_unit = models.BooleanField(default=True)

    def __str__(self):
        if self.display_unit:
            return f"{self.recipe} / {self.value} {self.unit} {self.ingredient}"
        return f"{self.recipe} / {self.value} {self.ingredient}"
