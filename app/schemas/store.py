from pydantic import BaseModel

class StoreBase(BaseModel):
    name: str 
    phone: str 

class StoreCreate(StoreBase):
    pass

class StoreResponse(StoreBase):
    id: int

    class Config:
        from_attributes = True 