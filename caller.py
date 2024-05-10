import os

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ORM_testing.settings")
django.setup()

from main_app.models import Car


def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        percentage_off = sum(int(x) for x in str(car.year)) / 100
        discount = float(car.price) * percentage_off
        car.price_with_discount = float(car.price) - discount
        car.save()


apply_discount()
