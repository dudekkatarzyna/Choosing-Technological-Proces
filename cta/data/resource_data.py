from dataclasses import dataclass


@dataclass
class ResourceData:
    length: float
    amount: int
    exact_amount: bool
