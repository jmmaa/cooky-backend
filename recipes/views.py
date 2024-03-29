import io

from django.core import serializers

from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


from django.core.paginator import Paginator

from recipes.serializers import RecipeSerializer

from .models import Recipe, UserRecipeCollection, UserRecipe


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_recipe(request):
    recipe = Recipe.objects.create(**request.data)
    mapping = UserRecipe.objects.create(recipe=recipe, user=request.user)

    recipe.save()
    mapping.save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_recipe(request):
    id = request.data.get("id")

    if id is not None:
        Recipe.objects.filter(pk=id).delete()
        return Response(status=status.HTTP_200_OK)

    else:
        return Response(
            {"detail": "required id field"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_recipe(request):
    id = request.data.get("id")

    if id is not None:
        Recipe.objects.filter(pk=id).update(**request.data)

        return Response(status=status.HTTP_202_ACCEPTED)

    else:
        return Response(
            {"detail": "required id field"}, status=status.HTTP_400_BAD_REQUEST
        )


# for search page
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_user_recipes(request):
    page = request.GET.get("page")

    if page is not None:
        all_recipes = Recipe.objects.all()
        pagination = Paginator(all_recipes, 10)
        recipes = pagination.page(page).object_list

        json = serializers.serialize("json", recipes)
        stream = io.BytesIO(json.encode())
        data = JSONParser().parse(stream)

        return Response(
            {
                "count": pagination.count,
                "num_pages": pagination.num_pages,
                "results": data,
            }
        )

    else:
        all_recipes = Recipe.objects.all()
        pagination = Paginator(all_recipes, 10)
        recipes = pagination.page(1).object_list

        json = serializers.serialize("json", recipes)
        stream = io.BytesIO(json.encode())
        data = JSONParser().parse(stream)

        return Response(
            {
                "count": pagination.count,
                "num_pages": pagination.num_pages,
                "results": data,
            }
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_user_recipes_by_user(request):
    page = request.GET.get("page")

    if page is not None:
        user_recipes = Recipe.objects.filter(userrecipe__user=request.user)

        pagination = Paginator(user_recipes, 10)
        recipes = pagination.page(page).object_list

        data = RecipeSerializer(recipes, many=True).data

        return Response(
            {
                "count": pagination.count,
                "num_pages": pagination.num_pages,
                "results": data,
            }
        )

    else:
        user_recipes = Recipe.objects.filter(userrecipe__user=request.user)

        pagination = Paginator(user_recipes, 10)
        recipes = pagination.page(1).object_list

        data = RecipeSerializer(recipes, many=True).data

        return Response(
            {
                "count": pagination.count,
                "num_pages": pagination.num_pages,
                "results": data,
            }
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_user_recipe_collections_by_user(request):
    page = request.GET.get("page")

    if page is not None:
        all_results = Recipe.objects.filter(
            userrecipe__userrecipecollection__user=request.user
        )
        # all_results = UserRecipeCollectionMapping.objects.filter(user=request.user)
        pagination = Paginator(all_results, 10)
        results = pagination.page(page).object_list

        json = serializers.serialize("json", results)
        stream = io.BytesIO(json.encode())
        data = JSONParser().parse(stream)

        return Response(
            {
                "count": pagination.count,
                "num_pages": pagination.num_pages,
                "results": data,
            }
        )

    else:
        all_results = Recipe.objects.filter(
            userrecipe__userrecipecollection__user=request.user
        )
        pagination = Paginator(all_results, 10)
        results = pagination.page(1).object_list

        json = serializers.serialize("json", results)
        stream = io.BytesIO(json.encode())
        data = JSONParser().parse(stream)

        return Response(
            {
                "count": pagination.count,
                "num_pages": pagination.num_pages,
                "results": data,
            }
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_user_recipe_to_collection_by_user(request):
    user_recipe_id = request.data.get("user_recipe_id")

    if user_recipe_id is not None:
        user_recipe = UserRecipe.objects.get(pk=user_recipe_id)
        mapping = UserRecipeCollection.objects.create(
            user_recipe=user_recipe, user=request.user
        )

        mapping.save()

        return Response(status=status.HTTP_201_CREATED)

    else:
        return Response(
            {"detail": "required user_recipe_id field"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_user_recipe_to_collection_by_user(request):
    user_recipe_id = request.data.get(
        "user_recipe_id"
    )  # or maybe i shud get collection id? idk

    if user_recipe_id is not None:
        user_recipe = UserRecipe.objects.get(pk=user_recipe_id)

        mapping = UserRecipeCollection.objects.get(
            user=request.user, user_recipe=user_recipe
        )

        mapping.delete()

        return Response(status=status.HTTP_200_OK)

    else:
        return Response(
            {"detail": "required user_recipe_id field"},
            status=status.HTTP_400_BAD_REQUEST,
        )
