"""Главный модуль CLI-приложения ассемблера."""

import argparse
import sys
from assembler import load_source, translate_to_ir


def parse_arguments() -> argparse.Namespace:
    """Парсит аргументы командной строки."""
    parser = argparse.ArgumentParser(
        description="Ассемблер для УВМ (Этап 1)."
    )
    parser.add_argument(
        "--source", "-s", type=str, required=True,
        help="Путь к исходному файлу с текстом программы (JSON)."
    )
    parser.add_argument(
        "--output", "-o", type=str, required=True,
        help="Путь к двоичному файлу-результату."
    )
    parser.add_argument(
        "--test-mode", "-t", action="store_true",
        help="Режим тестирования (вывод полей и значений)."
    )
    return parser.parse_args()


def print_ir(ir: list) -> None:
    """Выводит промежуточное представление в формате тестов."""
    for item in ir:
        if item["B"] == 0:
            print(f"Тест (A={item['A']}):")
        else:
            print(f"Тест (A={item['A']}, B={item['B']}):")


def main() -> None:
    """Главная функция приложения."""
    args = parse_arguments()

    try:
        source = load_source(args.source)
        ir = translate_to_ir(source)
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

    if args.test_mode:
        print_ir(ir)
    else:
        print(f"Программа успешно прочитана. Команд: {len(ir)}.")
        print(f"Выходной файл {args.output} будет создан на Этапе 2.")


if __name__ == "__main__":
    main()