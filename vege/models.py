from django.db import models
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="List ingredients separated by commas.")
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Cooking time in minutes.")
   
  


