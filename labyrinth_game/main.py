#!/usr/bin/env python3
"""Основной модуль игры Лабиринт сокровищ."""

# Просто импортируем constants из той же папки
import constants


def main():
    """Основная функция игры Лабиринт сокровищ."""
    print("Первая попытка запустить проект!")
    
    # Демонстрация доступа к импортированным константам
    print(f"\n🎮 {constants.GAME_TITLE}")
    print(f"Стартовая комната: {constants.START_ROOM}")
    print(f"Доступные направления: {', '.join(constants.DIRECTIONS)}")
    print(f"Доступные команды: {', '.join(constants.COMMANDS)}")
    
    # Информация о стартовой комнате
    start_room = constants.ROOMS[constants.START_ROOM]
    print(f"\n📍 {constants.START_ROOM.title()}:")
    print(f"   {start_room['description']}")
    print(f"   Выходы: {list(start_room['exits'].keys())}")
    print(f"   Предметы: {start_room['items']}")
    
    print(f"\nУсловие победы: найти {constants.WIN_CONDITION}!")
    print(f"Всего комнат в лабиринте: {len(constants.ROOMS)}")


if __name__ == "__main__":
    main()