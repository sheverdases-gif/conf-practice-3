"""Модуль трансляции языка ассемблера (JSON) в промежуточное представление."""

import json

OPCODES = {
    "load_const": 11,
    "read_mem": 8,
    "write_mem": 10,
    "sgn": 1
}


def load_source(file_path: str) -> list:
    """Читает JSON-файл с программой."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Файл программы не найден: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Ошибка: файл программы содержит некорректный JSON.")


def translate_to_ir(source_data: list) -> list:
    """
    Переводит исходный JSON в промежуточное представление.
    Возвращает список словарей с полями A и B.
    """
    ir = []
    for item in source_data:
        cmd = item.get("command")
        if cmd not in OPCODES:
            raise ValueError(f"Неизвестная команда: {cmd}")
        
        a_field = OPCODES[cmd]
        b_field = item.get("operand", 0)
        
        ir.append({"A": a_field, "B": b_field})
    
    return ir
