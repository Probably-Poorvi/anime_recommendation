from fastapi import FastAPI
from .database import Base, engine
from .auth.routes import router as auth_router
from .anime.routes import router as anime_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static directory to serve static files like favicon.ico
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Anime Recommendation System"}

@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("static/favicon.ico")
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(anime_router)
