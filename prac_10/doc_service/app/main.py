from fastapi import FastAPI, HTTPException

from app.phone import Phone

phones: list[Phone] = [
    Phone(0, 'Amazon Fire Phone', 'Amazon'),
    Phone(1, 'Asus PadFone', 'Asus'),
    Phone(2, 'BlackBerry Priv', 'BlackBerry Limited'),
    Phone(3, 'HTC Dream', 'HTC'),
    Phone(4, 'Honor 9', 'Huawei')
]

app = FastAPI()


@app.get("/v1/phones")
async def get_phones():
    return phones


@app.get("/v1/phones/{id}")
async def get_phone_by_id(id: int):
    result = [item for item in phones if item.id == id]
    if len(result) > 0:
        return result
    raise HTTPException(status_code=404, detail="Phone not found")
