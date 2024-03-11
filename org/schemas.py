
from pydantic import BaseModel
from typing import Union, List

class OrgContact(BaseModel):
    email: str
    phone: str 
    hours: str

class TeamMember(BaseModel):
    name: str 
    image: str
    position: str
    social_media_links: Union[List[str], None] = None

class FAQ(BaseModel):
    question: str 
    answer: str

class GalleryItem(BaseModel):
    heading: str 
    image: str 
    description: str 

class OrgIn(BaseModel):
    name: str 
    about: Union[str, None] = None
    location: Union[str, None] = None
    contacts: Union[OrgContact, None] = None
    welcome_message: Union[str, None] = None
    background: Union[str, None] = None
    mission: Union[str, None] = None
    vision: Union[str, None] = None
    core_values: Union[List[str], None] = None
    team_members: Union[List[TeamMember], None] = None
    faqs: Union[List[FAQ], None] = None
    gallery: Union[List[GalleryItem], None] = None


class OrgOut(OrgIn):
    id: int

# class OrgCreateError(BaseModel):
#     message: str
