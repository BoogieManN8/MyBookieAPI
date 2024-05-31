import os

class Settings:
    PROJECT_NAME: str = "MyBookieBackend"
    SQLALCHEMY_DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://skugge:GhostChaser8@db/mybookie")

settings = Settings()
