from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/', recipe_list, name='list'),
    path('recipe/<str:recipe_name>/', recipe_detail, name='detail'),
]

app_name = "ledger"