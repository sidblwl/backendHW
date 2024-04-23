from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel  #Base class for any class whose objects are used as input to a http request

todo_list_items = []

@app.get('/items')
async def root():
    return todo_list_items

class Item(BaseModel):
    name: str
    description: str

class Element(BaseModel):
    number: int

@app.post('/add')
async def add_item(item: Item):
    todo_list_items.append(item.name)
    return {'message': 'success'}

@app.delete('/remove')
async def remove_item(element: Element):
    todo_list_items.pop()
    return {'message': 'success'}