import os

import django
from django.db.models import QuerySet

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


# apply_discount()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


# print(get_recent_cars())
# print(get_recent_cars().count())

def delete_last_car() -> None:
    # print('Cars count before delete the last one: ')
    # print(Car.objects.all().count())
    Car.objects.last().delete()


# delete_last_car()
# print('Cars count after deleting the last one: ')
# print(Car.objects.all().count())
