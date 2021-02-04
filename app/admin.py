from django.contrib import admin

from app.models import Recipe, Ingredient, Unit, RecipeIngredientUnit


class RecipeIngredientUnitInlineAdmin(admin.TabularInline):
    model = RecipeIngredientUnit
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    fields = ("title",)
    inlines = (RecipeIngredientUnitInlineAdmin,)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
