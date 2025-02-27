from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "task_lists.html", {"recipes": recipes})

def recipe_detail(request, recipe_name):
    recipes = Recipe.objects.all()
    recipe_list = None
    for recipe in recipes:
        if recipe.name == recipe_name:
            recipe_list = recipe
    return render(request, "task_list.html", {"recipe": recipe_list})    

