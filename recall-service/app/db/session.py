from sqlalchemy import create_engine,select
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db_model.predictions import DBPrediction
from app.schema.recall import RecallMessage

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == '__main__':
    version_id=1
    segment_id=None
    tp = 0
    fn = 0

    ### Note: this entire thing can be done in SQL. including the counts of tp and fn and the recall claculation. I need more time to convert this lofic to sqlalchemy statment. couldn't do it on the fly.
    stmt = select(DBPrediction).where(DBPrediction.version_id==version_id)
    if segment_id is not None:
        stmt = stmt.where(DBPrediction.segment_id==segment_id)
    with SessionLocal() as session:
        results = session.execute(stmt).scalars()
        for pred in results:
            if pred.prediction_value==1 and pred.actual_obj.actual_value==1:
                tp+=1
            if pred.prediction_value==0 and pred.actual_obj.actual_value==1:
                fn+=1
    message = RecallMessage(Version_id=version_id, Segment_id=segment_id, Recall=1.0*tp/(tp+fn))
    pass

