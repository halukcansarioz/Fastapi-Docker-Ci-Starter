from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Docker CI Starter")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


items_db: dict[int, Item] = {}
next_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    item_id = next_id
    items_db[item_id] = item
    next_id += 1
    return {"id": item_id, **item.model_dump()}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items_db[item_id].model_dump()}
