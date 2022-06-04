from fastapi import FastAPI
from .routers import heroes

app = FastAPI()
app.include_router(heroes.router)

@app.get("/")
async def root():
    return {"message": "This is root"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
