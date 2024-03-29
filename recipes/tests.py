from datetime import datetime

from django.test import TransactionTestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from .models import Recipe, UserRecipeMapping, UserRecipeCollectionMapping
# Create your tests here.


class TestModel(TransactionTestCase):
    def setUp(self) -> None:
        Recipe.objects.create(
            name="adobo",
            number_of_servings=2,
            preparation_time=datetime.now(),
            ingredients="",
            procedure="",
        ).save()

        Recipe.objects.create(
            name="sinigang",
            number_of_servings=1,
            preparation_time=datetime.now(),
            ingredients="",
            procedure="",
        ).save()

        User.objects.create(username="test_username_1", password="test_password").save()
        User.objects.create(username="test_username_2", password="test_password").save()
        User.objects.create(username="test_username_3", password="test_password").save()
        User.objects.create(username="test_username_4", password="test_password").save()

    def test_queries(self):
        recipe_1 = Recipe.objects.get(name="adobo")
        recipe_2 = Recipe.objects.get(name="sinigang")

        author_1 = User.objects.get(username="test_username_1")
        author_2 = User.objects.get(username="test_username_2")

        recipe_1_with_author_1 = UserRecipeMapping(user=author_1, recipe=recipe_1)
        recipe_1_with_author_1.save()

        assert recipe_1_with_author_1.user.username == "test_username_1"

        recipe_2_with_author_1 = UserRecipeMapping(user=author_1, recipe=recipe_2)
        recipe_2_with_author_1.save()

        assert recipe_2_with_author_1.user.username == "test_username_1"

        recipe_1_with_author_2 = UserRecipeMapping(user=author_2, recipe=recipe_1)
        with self.assertRaises(IntegrityError):
            recipe_1_with_author_2.save()

        user_3 = User.objects.get(username="test_username_3")
        user_4 = User.objects.get(username="test_username_4")

        collection_user_3 = UserRecipeCollectionMapping(
            user=user_3, user_recipe=recipe_1_with_author_1
        )

        collection_user_3.save()

        collection_user_3 = UserRecipeCollectionMapping(
            user=user_3, user_recipe=recipe_2_with_author_1
        )
        collection_user_3.save()

        collection_user_4 = UserRecipeCollectionMapping(
            user=user_4, user_recipe=recipe_1_with_author_1
        )
        collection_user_4.save()

        collection_user_4 = UserRecipeCollectionMapping(
            user=user_4, user_recipe=recipe_2_with_author_1
        )
        collection_user_4.save()
