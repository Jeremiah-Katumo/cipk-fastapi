from fastapi import FastAPI, status, HTTPException, Path, APIRouter
from typing import Annotated, Union, List
from ..schemas import org_schemas
from ..cruds import  contact_us_cruds
from ...database import db_session

router = APIRouter(
    prefix="/contact_us",
    tags=['Contact']
)

@router.post("/{org_id}", status_code=status.HTTP_201_CREATED, response_model=org_schemas.ContactMessageOut)
def create_org_message(db: db_session, message: org_schemas.ContactMessageIn):
    message = contact_us_cruds.create_message(db, message)
    return message


@router.get("/", response_model=List[org_schemas.ContactMessageOut])
def get_org_messages(
    db: db_session, 
    org_id: int, 
    status: org_schemas.MessageStatus, 
    offset: Union[int, None] = 0, 
    limit: Union[Annotated[int, Path(le=10)], None] = 10
    ):
    messages = contact_us_cruds.get_messages(db, org_id, status, offset, limit)
    return messages

@router.get("/{message_id}", response_model=org_schemas.ContactMessageOut)
def get_single_message(db: db_session, message_id: int):
    message = contact_us_cruds.get_single_message(db, message_id)
    return message

@router.put("/{message_id}", response_model=org_schemas.ContactMessageOut)
def update_message(db: db_session, message_id: int, message: org_schemas.ContactMessageIn):
    message = contact_us_cruds.update_message(db, message_id, message)
    return message
