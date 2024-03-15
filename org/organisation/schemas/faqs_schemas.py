from fastapi import UploadFile
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Union, List
from enum import Enum
from uuid import UUID

class Faq(BaseModel):
    question: str 
    answer: str
    
class FAQs(BaseModel):
    faqs: Union[List[Faq], None] = None