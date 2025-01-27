from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
def home(request):
    if request.method == 'POST':  
        return redirect('/add_recipe/')  

    return render(request, 'home.html')  
def add_recipe(request, recipe_id=None):
    recipe = None
    if recipe_id:
        recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        ingredients = request.POST.get("ingredients")
        instructions = request.POST.get("instructions")
        cooking_time = request.POST.get("cooking_time")
        Recipe.objects.create(
                title=title,
                description=description,
                ingredients=ingredients,
                instructions=instructions,
                cooking_time=cooking_time,
            )
      
            
        return redirect("add_recipe")

    recipes = Recipe.objects.all()
    return render(request, "recipes.html", {"recipe": recipe, "recipes": recipes})


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect("add_recipe")

def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        recipe.title = request.POST.get("title")
        recipe.description = request.POST.get("description")
        recipe.ingredients = request.POST.get("ingredients")
        recipe.instructions = request.POST.get("instructions")
        recipe.cooking_time = request.POST.get("cooking_time")
        recipe.save()
        return redirect("/add_recipe/")

    return render(request, "update.html", {"recipe": recipe})