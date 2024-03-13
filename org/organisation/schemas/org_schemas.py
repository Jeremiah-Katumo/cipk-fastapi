
from fastapi import UploadFile
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Union, List
from enum import Enum
from uuid import UUID

class Positions(str, Enum):
    director = "Director"
    pc = "Project Cordinator"

class MessageStatus(str, Enum):
    all = "all"
    new = "new"
    replied = "replied"

class OrgContact(BaseModel):
    email: Union[EmailStr, None] = None
    phone: Union[str, None] = None 
    hours: Union[str, None] = None 

class TeamMember(BaseModel):
    name: str 
    image: UploadFile
    position: Positions
    social_media_links: Union[List[str], None] = None

class FAQ(BaseModel):
    question: str 
    answer: str

class GalleryItem(BaseModel):
    heading: str 
    image: UploadFile 
    description: str 

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


class ContactMessageIn(BaseModel):
    name: str 
    org_id: int
    email: EmailStr 
    subject: str 
    message: str

    class Config:
        orm_mode = True

class ContactMessageOut(ContactMessageIn):
    id: int
    org_id: int
    status: Union[str, None] = 'new'
    created_date: Union[date, None] = None 
    updated_date: Union[date, None] = None
    created_by: Union[int, None] = None 
    updated_by: Union[int, None] = None 

    class Config:
        orm_mode = True

class OrgOut(OrgIn):
    id: int
    messages: list[ContactMessageOut]
    created_date: Union[date, None] = None 
    updated_date: Union[date, None] = None
    created_by: Union[int, None] = None 
    updated_by: Union[int, None] = None 
    org_status: Union[str, None] = 'active'

    class Config:
        orm_mode = True