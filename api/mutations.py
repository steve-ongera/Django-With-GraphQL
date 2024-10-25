import graphene
from .models import Ingredient, Category
from graphene_django.types import DjangoObjectType

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class IngredientInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    category_id = graphene.ID(required=True)

class CreateMultipleIngredients(graphene.Mutation):
    class Arguments:
        ingredients = graphene.List(IngredientInput, required=True)

    ingredients = graphene.List(IngredientType)

    def mutate(self, info, ingredients):
        created_ingredients = []
        for ingredient_data in ingredients:
            category = Category.objects.get(id=ingredient_data.category_id)
            ingredient = Ingredient.objects.create(
                name=ingredient_data.name,
                category=category
            )
            created_ingredients.append(ingredient)

        return CreateMultipleIngredients(ingredients=created_ingredients)

class Mutation(graphene.ObjectType):
    create_multiple_ingredients = CreateMultipleIngredients.Field()
