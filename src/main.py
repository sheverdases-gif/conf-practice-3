"""Главный модуль CLI-приложения ассемблера."""

import argparse
import sys
from assembler import load_source, translate_to_ir
from codegen import generate_machine_code


def parse_arguments() -> argparse.Namespace:
    """Парсит аргументы командной строки."""
    parser = argparse.ArgumentParser(
        description="Ассемблер для УВМ (Этап 2)."
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
        help="Режим тестирования (вывод байтов)."
    )
    return parser.parse_args()


def print_hex_bytes(machine_code: bytes) -> None:
    """Выводит байты в формате 0xXX, как в тестах."""
    for i in range(0, len(machine_code), 3):
        chunk = machine_code[i:i+3]
        hex_str = ", ".join([f"0x{b:02X}" for b in chunk])
        print(hex_str)


def save_to_file(machine_code: bytes, file_path: str) -> None:
    """Сохраняет байты в двоичный файл."""
    try:
        with open(file_path, "wb") as f:
            f.write(machine_code)
        print(f"Размер файла: {len(machine_code)} байт.")
    except IOError as e:
        raise ValueError(f"Ошибка записи файла: {e}")


def main() -> None:
    """Главная функция приложения."""
    args = parse_arguments()

    try:
        source = load_source(args.source)
        ir = translate_to_ir(source)
        machine_code = generate_machine_code(ir)

        if args.test_mode:
            print_hex_bytes(machine_code)
        else:
            save_to_file(machine_code, args.output)

    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()