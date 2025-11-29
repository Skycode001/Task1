#!/usr/bin/env python3
"""Модуль с функциями для действий игрока."""


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