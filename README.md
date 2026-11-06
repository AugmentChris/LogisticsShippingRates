# Logistics Shipping Rates

[![CI](https://github.com/AugmentChris/LogisticsShippingRates/actions/workflows/ci.yml/badge.svg)](https://github.com/AugmentChris/LogisticsShippingRates/actions/workflows/ci.yml)

A command-line shipping cost calculator. You give it a package weight (kg) and a per-kg rate, and it returns the cost rounded to the cent.

## Features

- **Exact money math.** It uses Python's `Decimal` instead of floats, so `0.1 kg × $3` is `$0.30`, not `$0.30000000000000004`.
- **Input validation.** Rejects non-numbers, zero, negatives, `nan`, and `inf` with a clear message. In interactive mode it asks again instead of crashing.
- **Two modes.** Run it interactively, or pass the values as arguments for use in scripts.
- **Proper exit codes.** Returns 0 on success and 1 on bad input.

## Usage

Requires Python 3.8+. No dependencies.

```bash
python3 Shipping_Cost_Calculator.py
# Enter the package weight in kilograms: 2.5
# Enter the shipping rate per kilogram (USD): 4.20
# Shipping cost: $10.50 USD

python3 Shipping_Cost_Calculator.py 2.5 4.20
# Shipping cost: $10.50 USD
```

The core function can also be imported:

```python
from Shipping_Cost_Calculator import shipping_cost
shipping_cost("2.5", "4.20")  # Decimal('10.50')
```

## Tests

```bash
python3 -m unittest -v test_shipping_cost.py
```

CI runs the tests on Python 3.9 and 3.12 on every push.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Please keep the code style consistent, document new functions, and add tests for any change before opening a pull request.
