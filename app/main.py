from fastapi import FastAPI
from .routers import academy, controller, info, roster, solo, training_record, transfer

app = FastAPI()

app.include_router(info.router)


@app.get("/")
async def root():
    return {"message": "VATUSA Facility API"}
