from fastapi import FastAPI, status, HTTPException
from ..schemas import contact_us_schemas
from datetime import datetime, date
from ..models import org_models
from pydantic import parse_obj_as
from sqlalchemy.orm import Session
from sqlalchemy import desc


def create_message(db: Session, message: contact_us_schemas.ContactMessageIn):

    new_message = message.dict()
    org = db.query(org_models.Org).filter(org_models.Org.id == message.org_id).first() # .one() also works
    
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Org of id {message.org_id} not found')

    db_message = org_models.ContactMessage(**new_message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message


def get_messages(db, org_id: int, status: str, offset: int, limit: int):
    
    messages = []

    if status.value == 'all':
        messages = db.query(org_models.ContactMessage) \
            .order_by(desc(org_models.ContactMessage.created_date)) \
                .limit(limit).offset(offset).all()
    else:
        messages = db.query(org_models.ContactMessage) \
            .filter(org_models.ContactMessage.status == status.value) \
                .order_by(desc(org_models.ContactMessage.created_date)) \
                    .limit(limit).offset(offset).all()
    
    if len(messages) == 0:
        raise HTTPException(status_code=404, detail=f"No {status.value} message found for org Id {org_id}")

    return messages


def get_single_message(db: Session, message_id: int):
    message = db.query(org_models.ContactMessage).filter(org_models.ContactMessage.id == message_id).first() # .one() also works
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Message of id {message_id} not found')
    return message


def update_message(db: Session, message_id: int, message: contact_us_schemas.ContactMessageIn):
    request_message = message.dict()
    get_message = db.query(org_models.ContactMessage).filter(org_models.ContactMessage.id == message_id)
    new_message = get_message.first()

    if new_message == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Message of id {message_id} not found')
    
    to_update = {}
    
    for key, value in request_message.items():
        if request_message[key] != None:
            to_update[key] = value

    to_update.update({"updated_date": date.today()})
    get_message.update(to_update, synchronize_session=False)
    db.commit()

    return new_message

