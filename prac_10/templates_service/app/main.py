from fastapi import FastAPI, HTTPException

from app.laptop import Laptop

laptops: list[Laptop] = [
    Laptop(0, 'Lenovo', 'Hong Kong(China)'),
    Laptop(1, 'HP', 'United States'),
    Laptop(2, 'Dell', 'United States'),
    Laptop(3, 'Apple', 'United States'),
    Laptop(4, 'Walton', 'Bangladesh	')
]
    
app = FastAPI()


@app.get("/v1/laptops")
async def get_laptop():
    return laptops

@app.get("/v1/laptops/{id}")
async def get_laptop_by_id(id: int):
    result = [item for item in laptops if item.id == id]
    if len(result) > 0:
        return result
    raise HTTPException(status_code=404, detail="Laptop not found")