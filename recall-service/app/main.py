import asyncio

import uvicorn
from fastapi import FastAPI
from app.api.recall import recall
from app.core.config import settings
from app.db_model import Base
from app.db.session import engine
import logging

from app.queue.producer import producer

logging.basicConfig(level='DEBUG')

Base.metadata.create_all(bind=engine)

app = FastAPI(openapi_url=f"{settings.API_V1_STR}/recall/openapi.json", docs_url=f"{settings.API_V1_STR}/recall/docs")

app.include_router(recall, prefix=f'{settings.API_V1_STR}/recall', tags=['recall'])

if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0",port=8080)