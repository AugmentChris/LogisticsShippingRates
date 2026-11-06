"""Tests for the shipping cost calculator."""

import io
import unittest
from contextlib import redirect_stdout, redirect_stderr
from decimal import Decimal
from unittest.mock import patch

from Shipping_Cost_Calculator import main, shipping_cost


class TestShippingCost(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(shipping_cost(2.5, 4), Decimal("10.00"))

    def test_rounds_to_cents(self):
        self.assertEqual(shipping_cost("1.333", "3"), Decimal("4.00"))
        self.assertEqual(shipping_cost("0.125", "1"), Decimal("0.13"))

    def test_avoids_float_error(self):
        # 0.1 * 3 is 0.30000000000000004 in floating point
        self.assertEqual(shipping_cost("0.1", "3"), Decimal("0.30"))

    def test_rejects_invalid_values(self):
        for weight, rate in [("abc", 1), (-1, 5), (0, 5), (2, "nan"), (2, "inf"), ("", 1)]:
            with self.subTest(weight=weight, rate=rate), self.assertRaises(ValueError):
                shipping_cost(weight, rate)


class TestCli(unittest.TestCase):
    def run_main(self, argv, inputs=None):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err), patch("builtins.input", side_effect=inputs or []):
            code = main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_arguments(self):
        code, out, _ = self.run_main(["2.5", "4.20"])
        self.assertEqual(code, 0)
        self.assertIn("Shipping cost: $10.50 USD", out)

    def test_bad_argument(self):
        code, _, err = self.run_main(["heavy", "4"])
        self.assertEqual(code, 1)
        self.assertIn("must be a number", err)

    def test_interactive_reprompts(self):
        code, out, _ = self.run_main([], inputs=["abc", "-2", "2", "1500"])
        self.assertEqual(code, 0)
        self.assertIn("must be a number", out)
        self.assertIn("Shipping cost: $3,000.00 USD", out)


if __name__ == "__main__":
    unittest.main()
