from fastapi import FastAPI, status, HTTPException
from ..schemas import contact_us_schemas
from datetime import date

# from sqlalchemy.orm import Session


fakeMessagesDb = [
    {
        'id': 1,
        'org_id': 1,
        'name': 'Karisa',
        'email': 'nkmwambs@gmail.com',
        'status': 'new', # new, replied
        'created_date': '2024-03-10'
    }
]

# Contact US CRUDs

def create_message(org_id: int, message: contact_us_schemas.ContactMessageIn):

    message_ids = []
    new_message = message.dict()

    for fakeMessage in fakeMessagesDb:
        for key, value in fakeMessage.items():
            if(key == 'id'):
                message_ids.append(value)

    new_message.update({'id': int(message_ids[-1]) + 1, 'created_date': date.today(), 'status': 'new'})

    fakeMessagesDb.append(new_message)
    
    message = contact_us_schemas.ContactMessageOut(**new_message)

    # print(fakeMessagesDb)

    return message


def get_messages(org_id: int, status: str, limit: int, offset: int):

    messages = []

    for fakeMessage in fakeMessagesDb:
        for key, value in fakeMessage.items():
            if key == 'status' and value == 'new' and org_id == org_id:
                messages.append(fakeMessage)

    if len(messages) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No mesages found for the criteria provided")

    return messages


