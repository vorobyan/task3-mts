import threading
import webbrowser

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

from fastapi.responses import JSONResponse

app = FastAPI(
title="MTS-Task3-API",
description="A simple server that can handle two routes.",
version="1.0",
contact={
"name": "Daniil Vorobev",
"email": "daniil.vorobev951@gmail.com",
"url": "https://t.me/vorobyan",
}
)

class Item(BaseModel):
    key: str

@app.post("/inverse")
async def inverse(item: dict):
    swapped_dict = {value: key for key, value in item.items()}
    return JSONResponse(content=swapped_dict)

@app.get("/unstable")
async def unstable():
    if random.random() < 0.5:
        return {"message": "HAPPY"}
    else:
        raise HTTPException(status_code=400, detail="UNHAPPY")


def open_docs():
    webbrowser.open("http://127.0.0.1:8000/docs")


if __name__ == "__main__":
    threading.Timer(1, open_docs).start()

    # Запускаем приложение FastAPI
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

# Запуск сервера: uvicorn main:app --reload
