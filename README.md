# LottoCalculation - Lotto Bot

This small Python project provides a "lotto bot" that can generate lottery numbers using different strategies:

- Random generation (reproducible with a seed)
- Weighted generation based on historical draw frequencies (from a CSV file)

Quick start

1. Clone the repo and switch to main:

   git clone https://github.com/makeagamble/lottocalculation.git
   cd lottocalculation

2. Run the CLI

- Random draw (6 numbers from 1..49):

  python3 scripts/run_bot.py random

- Random draw with seed:

  python3 scripts/run_bot.py random --seed 42

- Weighted draw using sample history:

  python3 scripts/run_bot.py weighted --history sample_data/past_draws.csv

Notes

- The weighted strategy counts frequencies in the history CSV and biases selection toward numbers that appeared more often.
- The code uses only Python standard library (no external dependencies).
