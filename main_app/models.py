from django.db import models


class Pet(models.Model):
    name = models.CharField(
        max_length=40,
    )

    species = models.CharField(
        max_length=40,
    )


class Car(models.Model):
    model = models.CharField(
        max_length=40,
    )

    year = models.PositiveIntegerField()

    color = models.CharField(
        max_length=40,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    price_with_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )


class Task(models.Model):
    title = models.CharField(
        max_length=25,
    )

    description = models.TextField()

    due_date = models.DateField()

    is_finished = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"Task - {self.title} needs to be done until {self.due_date}!"


class HotelRoom(models.Model):
    ROOM_TYPES = [
        ("St", "Standard"),
        ("De", "Deluxe"),
        ("Su", "Suite"),
    ]
    room_number = models.PositiveIntegerField()

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES,
    )

    capacity = models.PositiveIntegerField()

    amenities = models.TextField()

    price_per_night = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    is_reserved = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.room_type} room with number {self.room_number} cost {self.price_per_night}$ price per night!"


class Character(models.Model):
    CHARACTER_CLASS_NAMES_CHOICES = [
        ('Ma', 'Mage'),
        ('Wa', 'Warrior'),
        ('As', 'Assassin'),
        ('Sc', 'Scout'),
    ]
    name = models.CharField(
        max_length=100,
    )

    class_name = models.CharField(
        choices=CHARACTER_CLASS_NAMES_CHOICES
    )

    level = models.PositiveIntegerField()

    strength = models.PositiveIntegerField()

    dexterity = models.PositiveIntegerField()

    intelligence = models.PositiveIntegerField()

    hit_points = models.PositiveIntegerField()

    inventory = models.TextField()
