
from fastapi import UploadFile, Form
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Union, List, Annotated
from enum import Enum
from uuid import UUID
from ..schemas import contact_us_schemas


class OrgContact(BaseModel):
    email: Union[EmailStr, None] = None
    phone: Union[str, None] = None 
    hours: Union[str, None] = None 



class OrgIn(BaseModel):
    name: Union[str, None] 
    org_uuid: Union[UUID, None] = None
    about: Union[str, None] = None
    location: Union[str, None] = None
    contacts: Union[OrgContact, None] = None
    welcome_message: Union[str, None] = None
    background: Union[str, None] = None
    mission: Union[str, None] = None
    vision: Union[str, None] = None
    core_values: Union[List[str], None] = None

    class Config:
        orm_mode = True


class OrgIn(BaseModel):
    name: Union[str, None] = None
    org_uuid: Union[UUID, None] = None
    about: Union[str, None] = None
    location: Union[str, None] = None
    contacts: Union[OrgContact, None] = None
    welcome_message: Union[str, None] = None
    background: Union[str, None] = None
    mission: Union[str, None] = None
    vision: Union[str, None] = None
    core_values: Union[List[str], None] = None

    class Config:
        orm_mode=True


class OrgOut(OrgIn):
    id: int
    messages: List[contact_us_schemas.ContactMessageOut]
    created_date: datetime
    updated_date: Union[date, None] = None
    created_by: Union[int, None] = None 
    updated_by: Union[int, None] = None 
    org_status: Union[str, None] = 'active'

    class Config:
        orm_mode=True

# class OrgCreateError(BaseModel):
#     message: str

# class ContactMessageIn(BaseModel):
#     name: str 
#     org_id: int
#     email: EmailStr 
#     subject: str 
#     message: str

# class ContactMessageOut(ContactMessageIn):
#     id: int
#     status: Union[str, None] = 'new'
#     created_date: date
#     updated_date: Union[datetime, None] = None
#     created_by: Union[int, None] = None 
#     updated_by: Union[int, None] = None 
