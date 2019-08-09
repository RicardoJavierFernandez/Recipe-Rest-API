from .models import Recipe, Step, Ingredient
from rest_framework import serializers


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ['step_text']


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['text']


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['user', 'name']


# class RecipeSerializer(serializers.ModelSerializer):
    # steps = StepSerializer(many=True)
    # ingredients = IngredientsSerializer(many=True)

    # class Meta:
    #     model = Recipe
    #     fields = ['user', 'name', 'steps']

    # def create(self, validated_data):
    #     steps_data = validated_data.pop('steps')
    #     recipe = Recipe.objects.create(**steps_data)
    #     for step_data in steps_data:
    #         Step.objects.create(recipe=recipe, **step_data)
    #     return recipe

