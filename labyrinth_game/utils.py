#!/usr/bin/env python3
"""Модуль с вспомогательными функциями для игры."""

import constants


def describe_current_room(game_state):
    """
    Выводит подробное описание текущей комнаты.
    
    Args:
        game_state (dict): Словарь с состоянием игры
    """
    current_room_name = game_state['current_room']
    room_data = constants.ROOMS[current_room_name]
    
    # Выводим название комнаты
    print(f"\n== {current_room_name.upper()} ==")
    
    # Выводим описание комнаты
    print(f"{room_data['description']}")
    
    # Выводим предметы, если они есть
    if room_data['items']:
        print("\n📦 Заметные предметы:")
        for item in room_data['items']:
            print(f"   - {item}")
    
    # Выводим доступные выходы
    if room_data['exits']:
        print("\n🚪 Выходы:")
        for direction, target_room in room_data['exits'].items():
            print(f"   {direction} → {target_room}")
    
    # Выводим информацию о загадке
    if room_data['puzzle'] is not None:
        print("\n❓ Кажется, здесь есть загадка (используйте команду solve).")


def get_available_directions(game_state):
    """
    Возвращает список доступных направлений из текущей комнаты.
    
    Args:
        game_state (dict): Словарь с состоянием игры
        
    Returns:
        list: Список доступных направлений
    """
    current_room_name = game_state['current_room']
    room_data = constants.ROOMS[current_room_name]
    return list(room_data['exits'].keys())


def room_has_puzzle(game_state):
    """
    Проверяет, есть ли в текущей комнате загадка.
    
    Args:
        game_state (dict): Словарь с состоянием игры
        
    Returns:
        bool: True если есть загадка, иначе False
    """
    current_room_name = game_state['current_room']
    room_data = constants.ROOMS[current_room_name]
    return room_data['puzzle'] is not None