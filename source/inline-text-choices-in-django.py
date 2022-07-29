# Want to support my work 😎? https://buymeacoffee.com/vandad

# in this example we create an inline text choice in for colors
# of a car and then assign them to the car without having
# to create a separate model for the color all together

from django.db import models


class Maker(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"Car maker, name = {self.name}, country = {self.country}"


class Car(models.Model):
    class Color(models.TextChoices):
        RED = ("RD",)
        BLUE = ("BL",)
        GREEN = ("GR",)
        BLACK = "BLK"

    maker = models.ForeignKey(
        Maker,
        on_delete=models.CASCADE,
    )
    color = models.TextField(choices=Color.choices)

    def __str__(self) -> str:
        return f"Car, maker = {self.maker}, color = {self.color}"
