import os

import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ORM_testing.settings")
django.setup()

from main_app.models import Car, Task, HotelRoom, Character, Pet


# Task 1
def create_pet(name: str, species: str) -> str:
    Pet.objects.create(
        name=name,
        species=species,
    )
    return f"{name} is a very cute {species}!"


print(create_pet('Buddy', 'Dog'))
print(create_pet('Whiskers', 'Cat'))
print(create_pet('Rocky', 'Hamster'))


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
# encode_and_replace('XXXXXX', 'Task 6')


def get_deluxe_room() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")

    return '\n'.join(str(room) for room in deluxe_rooms if room.id % 2 == 0)


#
# print(get_deluxe_room())


def reserve_first_room() -> None:
    return HotelRoom.objects.filter(id=1).update(is_reserved=True)

    # room = HotelRoom.objects.first()
    # room.is_reserved = True
    # room.save()


# reserve_first_room()


def delete_last_room() -> None:
    return HotelRoom.objects.filter(is_reserved=True).last().delete()

    # last_room = HotelRoom.objects.last()
    # if last_room.is_reserved:
    #     last_room.delete()


# delete_last_room()


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')
    previous_room_cap = None

    for room in rooms:
        if room.is_reserved:
            continue

        if previous_room_cap:
            room.capacity += previous_room_cap
        else:
            room.capacity = room.id

        previous_room_cap = room.capacity
        room.save()


# increase_room_capacity()


def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory="The inventory is empty",
    )


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + ' ' + second_character.name
    fusion_level = (first_character.level + second_character.level) // 2
    fusion_class = 'Fusion'
    fusion_strength = (first_character.strength + second_character.strength) * 1.2
    fusion_dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    fusion_intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    fusion_hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ['Mage', 'Scout']:
        fusion_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        fusion_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=fusion_name,
        class_name=fusion_class,
        level=fusion_level,
        dexterity=fusion_dexterity,
        strength=fusion_strength,
        intelligence=fusion_intelligence,
        hit_points=fusion_hit_points,
        inventory=fusion_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()

# character1 = Character.objects.create(
#     name="Gandalf",
#     class_name="Mage",
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory="Staff of Magic, Spellbook",
# )
#
# character2 = Character.objects.create(
#     name="Hector",
#     class_name="Warrior",
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory="Sword of Troy, Shield of Protection",
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
