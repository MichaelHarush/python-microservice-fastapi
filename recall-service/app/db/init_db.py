from session import engine
from app.db_model import Base
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    pass