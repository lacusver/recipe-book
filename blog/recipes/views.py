from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import *
from .forms import RecipeForm, RecipeListFormSet


def home(request):
    recipes = Recipes.objects.all()
    title = 'Recipes'
    context = {
        'recipes': recipes,
        'title': title
    }
    return render(request, template_name='recipes/home.html', context=context)


def get_recipe(request, slug):
    recipe = Recipes.objects.get(slug=slug)
    ingredients = recipe.recipelist_set.all()
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, template_name='recipes/recipe_detail.html', context=context)


def get_category(request, slug):
    recipes = Recipes.objects.filter(category__slug=slug)
    category = Categories.objects.get(slug=slug)
    context = {
        'recipes': recipes,
        'category': category
    }
    return render(request, template_name='recipes/recipes_by_category.html', context=context)


def search_ingr(request, slug=None):
    ingredients_list = request.GET.getlist('search-ing')
    if slug is not None:
        recipes = Recipes.objects.filter(category__slug=slug).filter(ingredients__title__icontains=ingredients_list[0])
    else:
        recipes = Recipes.objects.filter(ingredients__title__icontains=ingredients_list[0])
    for item in ingredients_list[1:]:
        recipes = recipes.filter(ingredients__title__icontains=item)
    context={
        'recipes': recipes
    }
    
    return render(request, template_name='recipes/search_ingr.html', context=context)


@login_required
def add_recipe(request):
    if request.method=='POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.slug = slugify(recipe.title)
            recipe = form.save()
            formset = RecipeListFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return redirect(recipe)
    else:
        form = RecipeForm()
        formset = RecipeListFormSet()
    return render(request, template_name='recipes/add_recipe.html', context={'form':form, 'formset':formset})

@login_required
def update_recipe(request, slug):
    recipe = Recipes.objects.get(slug=slug)
    if request.method=='POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.slug = slugify(recipe.title)
            recipe = form.save()
            formset = RecipeListFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return redirect(recipe)
    else:   
        form = RecipeForm(instance=recipe)
        formset = RecipeListFormSet(instance=recipe)
    return render(request, template_name='recipes/update_recipe.html', context={'form':form, 'formset':formset, 'slug':slug})

