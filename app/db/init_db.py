import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base 
from app.core.config import settings  


from app.models.match import Match
from app.models.log import Log

# Create an engine instance
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Session
db = SessionLocal()

def init_db():

    Base.metadata.create_all(bind=engine)
    print("All tables created successfully")

if __name__ == "__main__":
    init_db()
