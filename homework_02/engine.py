"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass(slots=True)
class Engine:
    volume: int
    pistons: int
