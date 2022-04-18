from django.contrib import admin
from recipes.models import Recipes, RecipeList, Ingredients, Categories


class RecipeListInline(admin.TabularInline):
    model = RecipeList
    extra = 1


class RecipesAdmin(admin.ModelAdmin):
    inlines = (RecipeListInline,)
    list_display = ('id', 'title', 'created_at', 'category', 'get_ingredients')
    prepopulated_fields = {'slug':('title',)}

class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Recipes, RecipesAdmin)
admin.site.register(RecipeList)
admin.site.register(Ingredients)
admin.site.register(Categories, CategoriesAdmin)


