#!/usr/bin/env python3

import argparse
import secrets
import random


def main(num_sellers: int, num_sales: int):
    names = ['Jude']
    relations = []

    for i in range(num_sellers):
        boss = random.choice(names)
        seller = secrets.token_hex(5)
        percentage = random.randint(1, 19) * 5
        names.append(seller)
        relations.append(f"{seller} {boss} {percentage}")

    if len(set(names)) != len(names):
        raise Exception("Failsafe triggered: Name collision")

    sales = []
    for i in range(num_sales):
        seller = random.choice(names)
        price = random.randint(1, 20000) * 100
        sales.append(f"{seller} {price}")

    random.shuffle(relations)
    random.shuffle(sales)

    print(len(relations))
    print("\n".join(relations))
    print(len(sales))
    print("\n".join(sales))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--sellers', type=int, required=True)
    parser.add_argument('--sales', type=int, required=True)
    args = parser.parse_args()
    main(args.sellers, args.sales)

