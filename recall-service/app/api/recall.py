import json
from typing import Optional
from dataclasses import asdict

from fastapi import APIRouter, status, Response
from sqlalchemy import select

from app.db.session import SessionLocal
from app.queue.logic import send_one
from app.db_model.predictions import DBPrediction
from app.schema.recall import RecallMessage

recall = APIRouter()

@recall.get('/version/{version_id}', status_code=status.HTTP_200_OK)
async def calculate_recall(version_id:int,segment_id: int|None=None):
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
    send_one(json.dumps(asdict(message)))
    return Response(json.dumps({'message': f'success calc recall for version {version_id} {f"and segment {segment_id}" if segment_id is not None else ""}'}))


