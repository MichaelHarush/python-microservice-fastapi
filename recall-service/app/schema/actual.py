
from pydantic.dataclasses import dataclass

@dataclass
class Actual:
    record_id: str
    actual_value: int

