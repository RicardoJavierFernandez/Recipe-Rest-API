from .models import Recipe, Step, Ingredient
from rest_framework import serializers


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ('id', 'step_text')
        read_only_fields = ('step_text',)


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'text')


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=False)
    ingredients = IngredientsSerializer(many=True, read_only=False)

    class Meta:
        model = Recipe
        fields = ('user',
                  'name',
                  'steps',
                  'steps',
                  'ingredients')

    def create(self, validated_data):
        steps_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)

        for step in steps_data:
            Step.objects.create(**step, recipe=recipe)

        for ingredient in ingredients_data:
            Ingredient.objects.create(**ingredient, recipe=recipe)

        return recipe

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance







