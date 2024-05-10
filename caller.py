import os

import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ORM_testing.settings")
django.setup()

from main_app.models import Car, Task


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


def show_undefined_task() -> str:
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return '\n'.join(str(t) for t in unfinished_tasks)


# print(show_undefined_task())


def complete_odd_task() -> None:
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
        task.save()


# complete_odd_task()


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(x)) for x in text)
    Task.objects.filter(title=task_title.lower()).update(description=decoded_text)


#     searching_tasks = Task.objects.filter(title=task_title.lower())
#     decoded_text = ''.join(chr(ord(x)) for x in text)
#
#     for task in searching_tasks:
#         task.description = decoded_text
#         task.save()
#
# encode_and_replace('asd$f323%#$3f#f3', 'Task - 1')
# encode_and_replace('111#$3f#f3', 'task 4')
# encode_and_replace('111#$3f#f3', 'Task 5')
encode_and_replace('XXXXXX', 'Task 6')
