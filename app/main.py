from fastapi import FastAPI
from app.api.routes import user, match, log

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(match.router, prefix="/matches", tags=["matches"])
app.include_router(log.router, prefix="/logs", tags=["logs"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MyBookieBackend"}
