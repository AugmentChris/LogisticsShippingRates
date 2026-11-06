"""Shipping cost calculator.

Computes the shipping cost of a package from its weight (kg) and a per-kg
rate. Run interactively, or pass the values as arguments:

    python Shipping_Cost_Calculator.py            # prompts for input
    python Shipping_Cost_Calculator.py 2.5 4.20   # weight, rate
"""

import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal("0.01")


def parse_positive(value, name):
    """Parse a positive decimal number, raising ValueError with a readable message."""
    try:
        number = Decimal(str(value).strip())
    except InvalidOperation:
        raise ValueError(f"{name} must be a number, got {value!r}.") from None
    if not number.is_finite() or number <= 0:
        raise ValueError(f"{name} must be greater than zero.")
    return number


def shipping_cost(weight_kg, rate_per_kg):
    """Return the shipping cost rounded to the nearest cent."""
    weight = parse_positive(weight_kg, "Weight")
    rate = parse_positive(rate_per_kg, "Rate")
    return (weight * rate).quantize(CENT, rounding=ROUND_HALF_UP)


def prompt_positive(prompt, name):
    """Ask until the user enters a valid positive number."""
    while True:
        try:
            return parse_positive(input(prompt), name)
        except ValueError as err:
            print(err)


def main(argv):
    """Entry point. Returns a process exit code."""
    if len(argv) == 2:
        try:
            cost = shipping_cost(argv[0], argv[1])
        except ValueError as err:
            print(f"Error: {err}", file=sys.stderr)
            return 1
    elif not argv:
        try:
            weight = prompt_positive("Enter the package weight in kilograms: ", "Weight")
            rate = prompt_positive("Enter the shipping rate per kilogram (USD): ", "Rate")
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return 1
        cost = shipping_cost(weight, rate)
    else:
        print("Usage: python Shipping_Cost_Calculator.py [weight_kg rate_per_kg]", file=sys.stderr)
        return 1

    print(f"Shipping cost: ${cost:,.2f} USD")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
