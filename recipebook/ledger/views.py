from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeIngredientForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


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

@login_required
def new_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        ingredient_form = RecipeIngredientForm(request.POST)

        if form.is_valid() and ingredient_form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = recipe  
            ingredient.save()

            return redirect("ledger:detail", recipe_name=recipe.name)
            
    else:
        form = RecipeForm()
        ingredient_form = RecipeIngredientForm()

    return render(request, "add_recipe.html", {"form": form, "ingredient_form": ingredient_form})

class AddRecipeImageView(CreateView):
    model = RecipeImage
    fields = ["image", "description"]
    template_name = "image.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs["pk"] 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("ledger:detail", kwargs={"recipe_name": self.object.recipe.name})