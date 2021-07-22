from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Recipe
from .forms import RecipeForm


def home(request):
    recipes = Recipe.objects.all()

    snack_recipes = Recipe.objects.filter(meal_type="SNACK")
    breakfast_recipes = Recipe.objects.filter(meal_type="BREAKFAST")
    lunch_recipes = Recipe.objects.filter(meal_type="LUNCH")
    dinner_recipes = Recipe.objects.filter(meal_type="DINNER")

    context = {
        'recipes': recipes,
        'recipe_types': [breakfast_recipes, lunch_recipes, dinner_recipes, snack_recipes],
        'title': 'Recipes - Home'
    }

    return render(
        request,
        "recipes/home.html",
        context=context
    )


def about(request):
    return render(
        request,
        "recipes/about.html",
        context={'title': 'Recipes - About'}
    )


def contact(request):
    return render(
        request,
        "recipes/contact.html",
        context={'title': 'Recipes - Contact'}
    )


@login_required
def details(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {
        'title': 'Recipe - Details',
        'recipe': recipe
    }
    return render(request, template_name="recipes/details.html", context=context)


@login_required
def add_recipe(request):

    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            # TODO: Clean data?
            form.save()
            return redirect('recipes-home')  # TODO: Make confirmation page

    else:
        form = RecipeForm

    return render(request, "recipes/add_recipe.html", context={'form': form, 'title': "Recipes - Add New"})


@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()

    return redirect('recipes-home')

