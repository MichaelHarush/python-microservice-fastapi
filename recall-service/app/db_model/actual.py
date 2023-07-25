
from sqlalchemy.orm import Mapped, mapped_column

from app.db_model.base import Base



class DBActual(Base):
    __tablename__ = "actual"

    record_id: Mapped[str] = mapped_column(primary_key=True)
    actual_value: Mapped[int]


