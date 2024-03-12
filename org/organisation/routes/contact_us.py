from fastapi import FastAPI, status, HTTPException, Path, APIRouter
from typing import Annotated, Union
from ..schemas import schemas
from ..cruds import  cruds


router = APIRouter(
    prefix="/contact_us",
    tags=['Contact']
)

@router.post("/{org_id}", status_code=status.HTTP_201_CREATED) # , response_model=schemas.ContactMessageOut
def contact_us(org_id: int, message: schemas.ContactMessageIn):
    cruds.create_message(org_id, message)
    return message


@router.get("/")
def get_messages(org_id: int, status: schemas.MessageStatus, limit: Union[int, None] = 0, offset: Union[int, None] = 10):
    
    messages = cruds.get_messages(org_id, status, limit, offset)

    return messages

@router.get("/{message_id}")
def get_message():
    return {'message': 'Get a message'}