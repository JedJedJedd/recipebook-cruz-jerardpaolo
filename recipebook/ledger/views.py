from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "task_lists.html", {"recipes": recipes})

@login_required
def recipe_detail(request, recipe_name):
    recipe = Recipe.objects.filter(name=recipe_name).first()
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(request, "task_list.html", {"recipe": recipe, "ingredients": ingredients})

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("ledger:list")  
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})
