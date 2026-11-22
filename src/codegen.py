"""Модуль генерации машинного кода из промежуточного представления."""

BYTE_MASK = 0xFF
NIBBLE_MASK = 0x0F


def generate_machine_code(ir: list) -> bytes:
    """
    Переводит промежуточное представление в последовательность байт.
    Возвращает объект bytes.
    """
    machine_code = bytearray()

    for item in ir:
        a_field = item["A"]
        b_field = item["B"]

        byte0 = (a_field & NIBBLE_MASK) | ((b_field & NIBBLE_MASK) << 4)
        byte1 = (b_field >> 4) & BYTE_MASK
        byte2 = (b_field >> 12) & BYTE_MASK

        machine_code.extend([byte0, byte1, byte2])

    return bytes(machine_code)