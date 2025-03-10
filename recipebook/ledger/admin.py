from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeIngredientInline(admin.TabularInline): 
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_on', 'updated_on')
    list_filter = ('author', 'created_on')
    search_fields = ('name',) 
    ordering = ('-created_on',)
    inlines = [RecipeIngredientInline]

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity')
    list_filter = ('recipe', 'ingredient')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient)
admin.site.register(Profile)