from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Recipe(models.Model):
    MEAL_CHOICES = [
        ("LUNCH", "Lunch"),
        ("BREAKFAST", "Breakfast"),
        ("DINNER", "Dinner"),
        ("SNACK", "Snack"),
        ("DESSERT", "Dessert")
    ]

    name = models.CharField(max_length=30)
    ingredients = models.TextField()
    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_CHOICES,
        default="Dinner"
    )
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    # slug = models.SlugField(null=True, blank=True)
    # image = models.ImageField()

    def __str__(self):
        return self.name
