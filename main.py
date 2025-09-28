#!/usr/bin/env python3
"""
Simple script: Fetch and display a random programming quote.
Perfect for a lightweight GitHub demo.
"""

import requests


def get_random_quote():
    url = "https://programming-quotesapi.vercel.app/api/random"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return f'"{data["en"]}" — {data["author"]}'


def main():
    try:
        print(get_random_quote())
    except Exception as e:
        print(f"Error fetching quote: {e}")


if __name__ == "__main__":
    main()
