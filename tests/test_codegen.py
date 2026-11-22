"""Тесты для модуля codegen."""

import sys
import os
import unittest

current_dir = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(current_dir, '..', 'src'))
sys.path.insert(0, src_path)

from codegen import generate_machine_code


class TestCodegen(unittest.TestCase):
    """Тесты трансляции в машинный код."""

    def test_load_const_bytes(self):
        """Тест: загрузка константы (тест из спецификации)."""
        ir = [{"A": 11, "B": 344}]
        expected = bytes([0x8B, 0x15, 0x00])
        self.assertEqual(generate_machine_code(ir), expected)

    def test_write_mem_bytes(self):
        """Тест: запись в память (тест из спецификации)."""
        ir = [{"A": 10, "B": 630}]
        expected = bytes([0x6A, 0x27, 0x00])
        self.assertEqual(generate_machine_code(ir), expected)

    def test_read_mem_and_sgn_bytes(self):
        """Тест: команды без операнда."""
        ir = [{"A": 8, "B": 0}, {"A": 1, "B": 0}]
        expected = bytes([0x08, 0x00, 0x00, 0x01, 0x00, 0x00])
        self.assertEqual(generate_machine_code(ir), expected)


if __name__ == "__main__":
    unittest.main()