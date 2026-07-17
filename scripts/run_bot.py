#!/usr/bin/env python3
"""CLI wrapper to run the lotto bot

Examples:
  python scripts/run_bot.py random --total 6 --pool-end 49
  python scripts/run_bot.py weighted --history sample_data/past_draws.csv --seed 1
"""
import argparse
from lotto_bot import generate_random_numbers, generate_weighted_from_history


def main():
    parser = argparse.ArgumentParser(description="Lotto bot CLI")
    sub = parser.add_subparsers(dest="mode", required=True)

    p_random = sub.add_parser("random", help="Generate purely random numbers")
    p_random.add_argument("--total", type=int, default=6)
    p_random.add_argument("--pool-start", type=int, default=1)
    p_random.add_argument("--pool-end", type=int, default=49)
    p_random.add_argument("--seed", type=int, default=None)

    p_weighted = sub.add_parser("weighted", help="Generate numbers based on history")
    p_weighted.add_argument("--history", type=str, required=True, help="Path to history CSV")
    p_weighted.add_argument("--total", type=int, default=6)
    p_weighted.add_argument("--pool-start", type=int, default=1)
    p_weighted.add_argument("--pool-end", type=int, default=49)
    p_weighted.add_argument("--seed", type=int, default=None)

    args = parser.parse_args()

    if args.mode == "random":
        nums = generate_random_numbers(total=args.total, pool_start=args.pool_start, pool_end=args.pool_end, seed=args.seed)
        print("Random draw:", nums)
    elif args.mode == "weighted":
        nums = generate_weighted_from_history(args.history, total=args.total, pool_start=args.pool_start, pool_end=args.pool_end, seed=args.seed)
        print("Weighted draw:", nums)


if __name__ == "__main__":
    main()
