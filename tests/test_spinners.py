# -*- coding: utf-8 -*-
"""This module tests Spinners enum."""
import re
import unittest

from enum import Enum
from spinners.spinners import Spinners


class TestSpinners(unittest.TestCase):
    """Test Spinners enum for attribute values."""

    def test_symbols(self):
        """Test the symbols in Spinners enum."""
        self.assertTrue(
            issubclass(Spinners, Enum)
        )

        dots = Spinners.dots

        self.assertEquals(
            dots.value['interval'], 80
        )

        self.assertEquals(
            type(dots.value['frames']), list
        )

if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestSpinners)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
