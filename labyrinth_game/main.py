#!/usr/bin/env python3
"""Основной модуль игры Лабиринт сокровищ."""

import constants
import utils


def main():
    """Основная функция игры Лабиринт сокровищ."""
    print("Первая попытка запустить проект!")
    
    # Состояние игры
    game_state = {
        'player_inventory': [],  # Инвентарь игрока
        'current_room': 'entrance',  # Текущая комната
        'game_over': False,  # Значение окончания игры
        'steps_taken': 0  # Количество шагов
    }
    
    # Демонстрация доступа к импортированным константам
    print(f"\n🎮 {constants.GAME_TITLE}")
    print(f"Стартовая комната: {constants.START_ROOM}")
    print(f"Доступные направления: {', '.join(constants.DIRECTIONS)}")
    print(f"Доступные команды: {', '.join(constants.COMMANDS)}")
    
    # СТАРЫЙ ВЫВОД (сохраняем)
    start_room = constants.ROOMS[game_state['current_room']]
    print(f"\n📍 {game_state['current_room'].title()}:")
    print(f"   {start_room['description']}")
    print(f"   Выходы: {list(start_room['exits'].keys())}")
    print(f"   Предметы: {start_room['items']}")
    
    # НОВЫЙ ВЫВОД (добавляем новую функцию)
    print("\n" + "="*50)
    print("📖 ПОДРОБНОЕ ОПИСАНИЕ КОМНАТЫ:")
    utils.describe_current_room(game_state)
    print("="*50)
    
    # Информация о состоянии игрока
    print("\n👤 Состояние игрока:")
    print(f"   Инвентарь: {game_state['player_inventory']}")
    print(f"   Шагов сделано: {game_state['steps_taken']}")
    print(f"   Игра завершена: {'Да' if game_state['game_over'] else 'Нет'}")
    
    # Демонстрация вспомогательных функций
    print(f"\n🧭 Доступные направления: {utils.get_available_directions(game_state)}")
    print(f"🎯 Есть загадка: {'Да' if utils.room_has_puzzle(game_state) else 'Нет'}")
    
    print(f"\n🎯 Условие победы: найти {constants.WIN_CONDITION}!")
    print(f"🏰 Всего комнат в лабиринте: {len(constants.ROOMS)}")


if __name__ == "__main__":
    main()