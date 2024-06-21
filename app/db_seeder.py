import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base  # Base should import all models
from app.core.config import settings  # Ensure this points to your settings file

# Import your models here to ensure they are registered with Base
from app.models.match import Match
from app.models.log import Log

# Create an engine instance
engine = create_engine(settings.DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Session
db = SessionLocal()

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("All tables created successfully")

if __name__ == "__main__":
    init_db()

print("TEST")
