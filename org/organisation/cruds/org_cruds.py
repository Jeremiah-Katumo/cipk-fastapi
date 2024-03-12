from fastapi import FastAPI, status, HTTPException
from ..schemas import org_schemas
from datetime import datetime, date

fakeDB = [
    {
        'id': 1,
        'name': 'CIPK',
        'created_date': '2024-03-12'
    }
]

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

# Org CRUDs

def get_org(org_id: int):
    org = None 

    for db_org in fakeDB:
        for key, value in db_org.items():
            if(key == 'id' and value == org_id):
                org = db_org
                break
    return org

def create_org(org: org_schemas.OrgIn):
    new_org = org.dict()
    
    orgIds = []

    for db_org in fakeDB:
        for key, value in db_org.items():
            if(key == 'id'):
                orgIds.append(value)
    
    new_org.update({'id': int(orgIds[-1]) + 1})

    fakeDB.append(new_org)

    org = new_org

    return org

def update_org(org_id: int, org: org_schemas.OrgIn):
    
    update_successful = False 
    new_org = org.dict()

    row = 0
    for db_org in fakeDB:
        for key, value in db_org.items():
            if(key == 'id' and value == org_id):
                new_org.update({'id': value})
                fakeDB[row] = new_org
                update_successful = True
            break
        row += 1 

    if not update_successful:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Org Id {org_id} not found')

    return new_org

# Contact US CRUDs

def create_message(org_id: int, message: org_schemas.ContactMessageIn):

    message_ids = []
    new_message = message.dict()

    for fakeMessage in fakeMessagesDb:
        for key, value in fakeMessage.items():
            if(key == 'id'):
                message_ids.append(value)

    new_message.update({'id': int(message_ids[-1]) + 1, 'created_date': date.today(), 'status': 'new'})

    fakeMessagesDb.append(new_message)
    
    message = org_schemas.ContactMessageOut(**new_message)

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


