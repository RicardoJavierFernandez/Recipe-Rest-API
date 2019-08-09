from rest_framework import viewsets
from .models import Recipe, Step, Ingredient
from .serializers import RecipeSerializer


class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
