from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import  ForeignKey

from app.db_model import DBActual
from app.db_model.base import Base

class DBPrediction(Base):
    __tablename__ = "predictions"

    version_id: Mapped[int]
    segment_id: Mapped[int]
    record_id: Mapped[str] = mapped_column(ForeignKey("actual.record_id"),primary_key=True)
    prediction_value: Mapped[int]
    actual_obj = relationship(DBActual, primaryjoin=record_id == DBActual.record_id)




