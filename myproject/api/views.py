from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Recipe
from .serializers import RecipeSerializer
import random

@api_view(['GET'])
def getData(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getDinners(request):
    recipes = Recipe.objects.filter(category="Dinner")
    random_recipe = random.choice(recipes)
    serializer = RecipeSerializer(random_recipe, many=False)

    return Response(serializer.data)
