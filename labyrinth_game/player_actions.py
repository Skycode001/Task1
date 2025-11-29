#!/usr/bin/env python3
"""Модуль с функциями для действий игрока."""

import constants
import utils


def show_inventory(game_state):
    """
    Отображает содержимое инвентаря игрока.
    
    Args:
        game_state (dict): Словарь с состоянием игры
    """
    inventory = game_state['player_inventory']
    
    print("\n🎒 ИНВЕНТАРЬ:")
    if inventory:
        for i, item in enumerate(inventory, 1):
            print(f"   {i}. {item}")
        print(f"\nВсего предметов: {len(inventory)}")
    else:
        print("   Инвентарь пуст")
        print("   Используйте команду 'take', чтобы подобрать предметы")


def get_input(prompt="> "):
    """
    Запрашивает ввод от пользователя с обработкой ошибок.
    
    Args:
        prompt (str): Текст приглашения для ввода
        
    Returns:
        str: Введенная пользователем строка или "quit" при ошибке
    """
    try:
        return input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def move_player(game_state, direction):
    """
    Перемещает игрока в указанном направлении.
    
    Args:
        game_state (dict): Словарь с состоянием игры
        direction (str): Направление для перемещения
    """
    current_room = game_state['current_room']
    room_data = constants.ROOMS[current_room]
    
    # Проверяем, существует ли выход в этом направлении
    if direction in room_data['exits']:
        # Обновляем текущую комнату
        game_state['current_room'] = room_data['exits'][direction]
        # Увеличиваем шаг на единицу
        game_state['steps_taken'] += 1
        # Выводим описание новой комнаты
        utils.describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")