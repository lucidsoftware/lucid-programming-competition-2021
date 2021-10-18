from collections import defaultdict
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class SellerBossRelationship:
    name: str
    boss: str
    percentage: int

    @staticmethod
    def from_line(line: str):
        name, boss, percentage_str = line.split()
        return SellerBossRelationship(
            name=name,
            boss=boss,
            percentage=int(percentage_str)
        )


@dataclass
class Sale:
    salesperson_name: str
    profit: int

    @staticmethod
    def from_line(line: str):
        name, profit_str = line.split()
        return Sale(
            salesperson_name=name,
            profit=int(profit_str)
        )


class PyramidProfitCalculator:

    def __init__(self, relationships: List[SellerBossRelationship]):
        self.root = 'Jude'
        self.sellers: Dict[str, SellerBossRelationship] = {
            relation.name: relation
            for relation in relationships
        }
        self.earnings: Dict[str, int] = defaultdict(float)

    @property
    def names(self):
        import itertools
        return sorted(itertools.chain(self.sellers.keys(), [self.root]))


    def get_boss_trace(self, seller: str) -> List[SellerBossRelationship]:
        # Traces the relationship from initial seller up layers of the Pyramid back to Jude
        # so we can figure out how much each person along the way is owed.

        trace: List[SellerBossRelationship] = []

        # You can also do this recursively, but it is probably slower
        #  and prone to overflowing the stack.
        while seller != self.root:
            trace.append(self.sellers[seller])
            seller = trace[-1].boss

        return trace


    def add_sale(self, sale: Sale):
        if sale.salesperson_name == self.root:
            self.earnings[self.root] += sale.profit
            return

        trace = self.get_boss_trace(sale.salesperson_name)

        # The reverse part is to make sure that Boss contracts are
        # honored first, and *then* the remainder is passed to the
        # subordinates.
        profit_remaining = sale.profit
        for relationship in reversed(trace):
            boss_cut = (1 / 100.0) * (100 - relationship.percentage) * profit_remaining
            profit_remaining -= boss_cut

            self.earnings[relationship.boss] += boss_cut

        # In real life, they say the boss gets paid last. In a pyramid though...
        #
        # This is why you don't want to be on the bottom of a Pyramid scheme :)
        self.earnings[trace[0].name] += profit_remaining


def main():
    num_salespeople = int(input())
    relationships = list([SellerBossRelationship.from_line(input()) for n in range(num_salespeople)])
    pyramid = PyramidProfitCalculator(relationships)

    num_sales = int(input())
    for n in range(num_sales):
        sale = Sale.from_line(input())
        pyramid.add_sale(sale)

    for name in sorted(pyramid.names):
        total_earnings = pyramid.earnings[name]

        # Students don't need this check, but I'm adding it to make sure that I didn't do something dumb
        if total_earnings >= 2 ** 32 - 1:
            raise Exception("Failsafe triggered: total earnings are too big in this test case, we need a new test case")

        print(name, round(pyramid.earnings[name]))


if __name__ == "__main__":
    main()