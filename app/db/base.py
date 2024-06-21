import os 
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app.db.base_class import Base
from app.models.user import User
from app.models.match import Match
from app.models.log import Log