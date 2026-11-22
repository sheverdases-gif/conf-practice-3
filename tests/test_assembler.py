"""Тесты для модуля assembler."""

import sys
import os
import unittest

current_dir = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(current_dir, '..', 'src'))
sys.path.insert(0, src_path)

from assembler import translate_to_ir


class TestAssembler(unittest.TestCase):
    """Тесты трансляции в промежуточное представление."""

    def test_translate_load_const(self):
        """Тест: загрузка константы."""
        source = [{"command": "load_const", "operand": 344}]
        ir = translate_to_ir(source)
        self.assertEqual(ir, [{"A": 11, "B": 344}])

    def test_translate_read_mem(self):
        """Тест: чтение из памяти."""
        source = [{"command": "read_mem"}]
        ir = translate_to_ir(source)
        self.assertEqual(ir, [{"A": 8, "B": 0}])

    def test_translate_unknown_command(self):
        """Тест: неизвестная команда вызывает ошибку."""
        source = [{"command": "invalid_cmd"}]
        with self.assertRaises(ValueError):
            translate_to_ir(source)


if __name__ == "__main__":
    unittest.main()
    