from dataclasses import is_dataclass
from pydantic.dataclasses import dataclass
@dataclass
class RecallMessage:
    Version_id: int
    Segment_id: int|None
    Recall: float

if __name__ == '__main__':
    m = RecallMessage(5,5,0.4)
    print(is_dataclass(m))
    pass