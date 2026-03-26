# This code allows you to store information on people owing you money
# and then list all those people in a ordered and formatted way in the terminal.
# Try to improve the `payday` function by splitting the logic into smaller functions.

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Debtor:
    """Stores the information on a person owing us money"""
    name: str
    debt: float

def sort_debtors_highest_first(debtors: Iterable[Debtor]) -> Iterable[Debtor]:
    """Sorts the debtors according to their debt, highest first"""
    return reversed(sorted(debtors, key=lambda debtor: debtor.debt))

def format_debtor(debtor: Debtor, threshold: float = 100.0) -> str:
    """Formats the debtor's information, highlighting if the debt is above a certain threshold"""
    output_str = f"{debtor.name}: "
    if debtor.debt > threshold:
        return output_str + f"!!!{debtor.debt}!!!"
    else:
        return output_str + f"{debtor.debt}"

def print_debtors(debtors: Iterable[Debtor]) -> None:
    for debtor in debtors:
        print(format_debtor(debtor))

def payday(debtors: Iterable[Debtor]) -> None:
    ordered = sort_debtors_highest_first(debtors)
    print_debtors(ordered)


if __name__ == "__main__":
    payday([
        Debtor("Person1", 100.0),
        Debtor("Person2", 200.0),
        Debtor("Person3", 10.0),
        Debtor("Person4", 50.0),
        Debtor("Person5", 1250.0)
    ])
