#!/usr/bin/env python3
"""Модуль с константами и неизменяемыми данными игры."""

ROOMS = {
    'entrance': {
        'description': (
            'Вы в темном входе лабиринта. Стены покрыты мхом. '
            'На полу лежит старый факел.'
        ),
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': (
            'Большой зал с эхом. По центру стоит пьедестал '
            'с запечатанным сундуком.'
        ),
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room'},
        'items': [],
        'puzzle': (
            'На пьедестале надпись: "Назовите число, которое идет после девяти". '
            'Введите ответ цифрой или словом.',
            '10'
        )
    },
    'trap_room': {
        'description': (
            'Комната с хитрой плиточной поломкой. На стене видна надпись: '
            '"Осторожно — ловушка".'
        ),
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': (
            'Система плит активна. Чтобы пройти, назовите слово "шаг" '
            'три раза подряд (введите "шаг шаг шаг")',
            'шаг шаг шаг'
        )
    },
    'library': {
        'description': (
            'Пыльная библиотека. На полках старые свитки. '
            'Где-то здесь может быть ключ от сокровищницы.'
        ),
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': (
            'В одном свитке загадка: "Что растет, когда его съедают?" '
            '(ответ одно слово)',
            'резонанс'
        )
    },
    'armory': {
        'description': (
            'Старая оружейная комната. На стене висит меч, '
            'рядом — небольшая бронзовая шкатулка.'
        ),
        'exits': {'south': 'library'},
        'items': ['sword', 'bronze_box', 'treasure_key'],
        'puzzle': None
    },
    'treasure_room': {
        'description': (
            'Комната, на столе большой сундук. '
            'Дверь заперта — нужен особый ключ.'
        ),
        'exits': {'south': 'hall'},
        'items': ['treasure_chest'],
        'puzzle': (
            'Дверь защищена кодом. Введите код '
            '(подсказка: это число пятикратного шага, 2*5= ? )',
            '10'
        )
    },
    # ДОБАВЛЕННЫЕ КОМНАТЫ:
    'garden': {
        'description': (
            'Тайный сад с волшебными растениями. '
            'В центре растет сияющий цветок.'
        ),
        'exits': {'east': 'hall', 'south': 'fountain'},
        'items': ['magic_flower', 'healing_potion'],
        'puzzle': (
            'Цветок шепчет: "Я легок как перо, '
            'но меня нельзя долго удержать. Что я?"',
            'дыхание'
        )
    },
    'fountain': {
        'description': (
            'Комната с мраморным фонтаном. '
            'Вода переливается всеми цветами радуги.'
        ),
        'exits': {'north': 'garden', 'west': 'secret_passage'},
        'items': ['crystal_vial'],
        'puzzle': (
            'На фонтане надпись: "Сколько цветов у радуги? '
            'Ответьте числом"',
            '7'
        )
    },
    'secret_passage': {
        'description': 'Узкий потайной ход. Стены покрыты древними символами.',
        'exits': {'east': 'fountain'},
        'items': ['golden_key', 'ancient_map'],
        'puzzle': None
    }
}

# Дополнительные константы
DIRECTIONS = ['north', 'south', 'east', 'west', 'up', 'down']
COMMANDS = ['go', 'look', 'take', 'inventory', 'use', 'solve', 'quit', 'help']
GAME_TITLE = "Лабиринт Сокровищ"
START_ROOM = 'entrance'
WIN_CONDITION = 'treasure_chest'