from django.urls import path

from .views import list, recipe1, recipe2
urlpatterns = [
    path('recipes/list/', list, name='list'),
    path('recipe/1/', recipe1, name='ingredient1'),
    path('recipe/2/', recipe2, name='ingredient2'),
]
# This might be needed, depending on your Django version
app_name = "ledger"