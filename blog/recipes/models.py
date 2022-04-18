from statistics import mode
from django.db import models
from django.urls import reverse


class Recipes(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, null=True)
    img = models.ImageField(upload_to='photos/recipes/%Y/%m/%d/', blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField('Ingredients', related_name='RecipeIngredients', through='RecipeList')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"slug": self.slug})
    

    def get_ingredients(self):
        return "\n".join([p.title for p in self.ingredients.all()])


class RecipeList(models.Model):
    recipe = models.ForeignKey('Recipes', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredients', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.recipe.title


class Ingredients(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Categories(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes-category", kwargs={"slug": self.slug})