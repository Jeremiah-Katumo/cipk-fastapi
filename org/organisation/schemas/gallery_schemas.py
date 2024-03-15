from fastapi import UploadFile
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Union, List
from enum import Enum
from uuid import UUID

class GalleryItem(BaseModel):
    heading: str 
    image: UploadFile 
    description: str
    
class Gallery(BaseModel):
    gallery: Union[List[GalleryItem], None] = None