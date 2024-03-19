from fastapi import UploadFile
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Union, List
from enum import Enum
from uuid import UUID

class MessageStatus(str, Enum):
    new = "New"
    replied = "Replied"

class ContactMessageIn(BaseModel):
    name: str 
    org_id: int
    email: EmailStr 
    subject: str 
    message: str
    # status: Union[List[MessageStatus], None] = None

    class Config:
        orm_mode=True

class ContactMessageOut(ContactMessageIn):
    id: int
    status: Union[str, None] = 'new'
    created_date: date
    updated_date: Union[datetime, None] = None
    created_by: Union[int, None] = None
    updated_by: Union[int, None] = None