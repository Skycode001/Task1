#!/usr/bin/env python3
"""Модуль с функции для действий игрока."""

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
        target_room = room_data['exits'][direction]
        
        # 🔒 ПРОВЕРКА ДОСТУПА К TREASURE_ROOM
        # Если пользователь переходит в treasure_room, проверяем наличие ключа
        if target_room == 'treasure_room':
            if 'rusty_key' in game_state['player_inventory']:
                # Если ключ есть, вывести сообщение и перевести в treasure_room
                message = (
                    "Вы используете найденный ключ, "
                    "чтобы открыть путь в комнату сокровищ."
                )
                print(message)
                game_state['current_room'] = target_room
                game_state['steps_taken'] += 1
                utils.describe_current_room(game_state)
                
                # 🔥 ИНТЕГРАЦИЯ ЛОВУШЕК
                trap_chance = utils.pseudo_random(game_state['steps_taken'], 100)
                if trap_chance < 15:
                    print("\n⚡️ ВНИМАНИЕ: При перемещении что-то щелкнуло...")
                    game_state['traps_triggered'] += 1
                    utils.trigger_trap(game_state)
                
                # 🎲 ИНТЕГРАЦИЯ СЛУЧАЙНЫХ СОБЫТИЙ
                utils.random_event(game_state)
            else:
                # В противном случае вывести сообщение
                print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
                return
        
        else:
            # Обычное перемещение в другие комнаты
            game_state['current_room'] = target_room
            game_state['steps_taken'] += 1
            utils.describe_current_room(game_state)
            
            # 🔥 ИНТЕГРАЦИЯ ЛОВУШЕК
            trap_chance = utils.pseudo_random(game_state['steps_taken'], 100)
            if trap_chance < 15:
                print("\n⚡️ ВНИМАНИЕ: При перемещении что-то щелкнуло...")
                game_state['traps_triggered'] += 1
                utils.trigger_trap(game_state)
            
            # 🎲 ИНТЕГРАЦИЯ СЛУЧАЙНЫХ СОБЫТИЙ
            utils.random_event(game_state)
    
    else:
        print("Нельзя пойти в этом направлении.")


def take_item(game_state, item_name):
    """
    Позволяет игроку подобрать предмет из комнаты.
    
    Args:
        game_state (dict): Словарь с состоянием игры
        item_name (str): Название предмета для взятия
    """
    # Если игрок пытается поднять или взять в инвентарь 'treasure_chest'
    if item_name == 'treasure_chest':
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return
    
    current_room = game_state['current_room']
    room_data = constants.ROOMS[current_room]
    
    # Проверяем, есть ли предмет в комнате
    if item_name in room_data['items']:
        # Добавляем предмет в инвентарь игрока
        game_state['player_inventory'].append(item_name)
        # Удаляем предмет из списка предметов комнаты
        room_data['items'].remove(item_name)
        # Печатаем сообщение о том, что игрок подобрал предмет
        print("Вы подняли:", item_name)
    else:
        print("Такого предмета здесь нет.")


def use_item(game_state, item_name):
    """
    Позволяет игроку использовать предмет из инвентаря.
    
    Args:
        game_state (dict): Словарь с состоянием игры
        item_name (str): Название предмета для использования
    """
    # Проверяем, есть ли предмет у игрока
    if item_name not in game_state['player_inventory']:
        print("У вас нет такого предмета.")
        return
    
    # Выполняем уникальное действие для каждого предмета
    match item_name:
        case 'torch':
            print("Вы зажигаете факел. Стало светлее.")
        
        case 'sword':
            print("Вы размахиваете мечом. Чувствуете себя увереннее.")
        
        case 'bronze_box':
            print("Вы открываете бронзовую шкатулку.")
            if 'rusty_key' not in game_state['player_inventory']:
                game_state['player_inventory'].append('rusty_key')
                print("Внутри вы находите rusty_key!")
            else:
                print("Шкатулка пуста.")
        
        case _:
            print("Вы не знаете, как использовать этот предмет.")