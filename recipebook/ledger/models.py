from django.db import models
from django.urls import reverse



class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger_detail', args=[str(self.name)])
        
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:detail', args=[str(self.name)])

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return self.quantity + " " + self.ingredient.name
    