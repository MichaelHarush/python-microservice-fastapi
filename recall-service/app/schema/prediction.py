from pydantic.dataclasses import dataclass

@dataclass
class Prediction:
    version_id: int
    segment_id: int
    record_id: str
    prediction_value: int



