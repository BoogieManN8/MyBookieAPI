from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all the models here
from app.models.user import User
from app.models.match import Match
from app.models.log import Log
