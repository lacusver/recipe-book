from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<str:slug>/', get_recipe, name='recipe-detail'),
    path('recipes/category/<str:slug>/', get_category, name='recipes-category'),
    path('search-ing/', search_ingr, name='search-ing' ),
    path('recipes/category/<str:slug>/search-ing/', search_ingr, name='search-ing-category'),
    path('recipes/add_recipe/', add_recipe, name='add-recipe'),
    path('recipes/update_recipe/<str:slug>/', update_recipe, name="update-recipe" )
]