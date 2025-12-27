from pydantic import BaseModel
from typing import List
from datetime import datetime

class AccountCreate(BaseModel):
    name: str

class TransactionBase(BaseModel):
    amount: float

class TransactionResponse(BaseModel):
    amount: float
    type: str
    timestamp: datetime

    class Config:
        orm_mode = True
