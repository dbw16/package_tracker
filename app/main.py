from fastapi import FastAPI
from app.routers import carriers, packages
import typing as t
from app.database import engine, Base, metadata

Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[])

app.include_router(carriers.router)
app.include_router(packages.router)
metadata.create_all(engine)


# Dependency
@app.get("/")
async def root() -> t.Any:
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    import uvicorn  # only for debugging

    uvicorn.run(app, host="0.0.0.0", port=8000)
