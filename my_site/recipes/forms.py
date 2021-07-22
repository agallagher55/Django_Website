from django.forms import ModelForm
from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'meal_type', 'author']
