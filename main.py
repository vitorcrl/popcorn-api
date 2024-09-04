from fastapi import FastAPI
from popcorn.routers import popcorn

app = FastAPI()
app.include_router(popcorn.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}