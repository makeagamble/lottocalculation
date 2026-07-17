"""Lotto bot core logic

Functions:
- generate_random_numbers
- generate_weighted_from_history

History file format: CSV where each row is a draw and numbers are comma-separated. Example:
10,23,35,36,41,44

"""
from typing import List, Optional
import random
import csv
import os


def generate_random_numbers(total: int = 6, pool_start: int = 1, pool_end: int = 49, seed: Optional[int] = None, unique: bool = True) -> List[int]:
    """Generate lotto numbers randomly.

    Args:
        total: How many numbers to draw.
        pool_start: Minimum number in pool (inclusive).
        pool_end: Maximum number in pool (inclusive).
        seed: Optional RNG seed for reproducibility.
        unique: Whether drawn numbers should be unique.

    Returns:
        Sorted list of drawn numbers.
    """
    if seed is not None:
        random.seed(seed)

    pool = list(range(pool_start, pool_end + 1))
    if unique:
        numbers = random.sample(pool, k=total)
    else:
        numbers = [random.choice(pool) for _ in range(total)]
    return sorted(numbers)


def generate_weighted_from_history(history_csv_path: str, total: int = 6, pool_start: int = 1, pool_end: int = 49, seed: Optional[int] = None) -> List[int]:
    """Generate numbers using frequencies from historical draws.

    The history CSV should have one draw per line with numbers separated by commas.
    If a number never appears in history, it still has weight 1.

    Args:
        history_csv_path: Path to CSV file with historical draws.
        total: How many numbers to draw.
        pool_start: Minimum number in pool (inclusive).
        pool_end: Maximum number in pool (inclusive).
        seed: Optional RNG seed for reproducibility.

    Returns:
        Sorted list of drawn numbers.
    """
    if seed is not None:
        random.seed(seed)

    counts = {n: 0 for n in range(pool_start, pool_end + 1)}

    if os.path.exists(history_csv_path):
        with open(history_csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # accept rows like "1,2,3,4,5,6" or rows with whitespace
                for v in row:
                    v = v.strip()
                    if not v:
                        continue
                    try:
                        num = int(v)
                    except ValueError:
                        continue
                    if pool_start <= num <= pool_end:
                        counts[num] += 1

    # build weights: frequency + 1 so zero-frequency numbers still have weight
    numbers = list(counts.keys())
    weights = [counts[n] + 1 for n in numbers]

    # Use random.choices to pick with replacement; we'll resample if duplicates appear
    chosen = set()
    attempts = 0
    max_attempts = 10000
    while len(chosen) < total and attempts < max_attempts:
        pick = random.choices(numbers, weights=weights, k=1)[0]
        chosen.add(pick)
        attempts += 1

    if attempts >= max_attempts and len(chosen) < total:
        # fallback to random unique sampling
        remaining = [n for n in numbers if n not in chosen]
        needed = total - len(chosen)
        chosen.update(random.sample(remaining, k=needed))

    return sorted(chosen)


if __name__ == "__main__":
    # simple demo
    print("Random draw:", generate_random_numbers(seed=42))
