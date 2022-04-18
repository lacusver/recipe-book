from django import template
from recipes.models import Ingredients, Categories

register = template.Library()

@register.inclusion_tag("recipes/search_tpl.html")
def search_ingr_bar (slug=None):
    ingredients = Ingredients.objects.all()
    return {
        "ingredients": ingredients,
        "slug" : slug
    }

@register.inclusion_tag("recipes/get_categories_tpl.html")
def get_categories():
    categories = Categories.objects.all()
    return{
        "categories": categories
    }
