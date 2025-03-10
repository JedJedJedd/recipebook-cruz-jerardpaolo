from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "task_lists.html", {"recipes": recipes})

def recipe_detail(request, recipe_name):
    recipes = Recipe.objects.filter(name=recipe_name).first()
    recipe_list = None
    for recipe in recipes:
        if recipe.name == recipe_name:
            recipe_list = recipe
    return render(request, "task_list.html", {"recipe": recipe})    

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("ledger:list")  
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})
