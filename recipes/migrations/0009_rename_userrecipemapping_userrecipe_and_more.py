# Generated by Django 5.0.3 on 2024-03-29 13:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_userrecipecollectionmapping_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserRecipeMapping',
            new_name='UserRecipe',
        ),
        migrations.RenameModel(
            old_name='UserRecipeCollectionMapping',
            new_name='UserRecipeCollection',
        ),
    ]
