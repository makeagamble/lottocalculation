# Lotto Bot

This branch adds a small Python lotto bot to generate lottery numbers.

Quick start:

1. Clone the repo and check out the branch:

   git clone https://github.com/makeagamble/lottocalculation.git
   cd lottocalculation
   git checkout lotto-bot

2. Run the CLI

- Random draw (6 numbers from 1..49):

  python3 scripts/run_bot.py random

- Random draw with seed:

  python3 scripts/run_bot.py random --seed 42

- Weighted draw using sample history:

  python3 scripts/run_bot.py weighted --history sample_data/past_draws.csv

Notes:

- The weighted strategy counts frequencies in the history CSV and biases selection toward numbers that appeared more often.
- The code uses only Python standard library (no external dependencies).

Files added:

- lotto_bot/bot.py: core logic
- scripts/run_bot.py: CLI
- sample_data/past_draws.csv: example history
- README.md, LICENSE, .gitignore

Merge instructions:

Review and if everything looks good, merge the branch `lotto-bot` into your default branch.
