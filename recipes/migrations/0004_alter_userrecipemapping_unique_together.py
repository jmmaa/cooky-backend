# Generated by Django 5.0.3 on 2024-03-27 15:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_image_alter_userrecipemapping_recipe_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userrecipemapping',
            unique_together={('user', 'recipe')},
        ),
    ]
