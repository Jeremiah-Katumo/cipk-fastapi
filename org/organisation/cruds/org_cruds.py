from fastapi import FastAPI, status, HTTPException
from ..schemas import org_schemas
from ..models import org_models
from pydantic import parse_obj_as
from sqlalchemy.orm import Session


def get_all_orgs(db, offset, limit):
    orgs = db.query(org_models.Org) \
        .order_by(desc(org_models.Org.created_date)) \
            .limit(limit).offset(offset).all()

    if len(orgs) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Org found")

    return orgs

def get_org(db: Session,org_id: int):
    org = db.query(org_models.Org).filter(org_models.Org.id == org_id).first() # .one() also works
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Org of id {org_id} not found')
    return org

def create_org(db: Session, org: org_schemas.OrgIn):

    new_org = org.dict()

    get_org = db.query(org_models.Org).filter(org_models.Org.name == org.name)
    org_in_db = get_org.first()

    if org_in_db !=  None:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail=f'Org with name {org.name} already exists')

    new_org.update({"created_date": date.today()})

    db_org = org_models.Org(**new_org)
    db.add(db_org)
    db.commit()
    db.refresh(db_org)

    return db_org

def update_org(db: Session, org_id: int, org: org_schemas.OrgIn):
    request_org = org.dict()

    get_org = db.query(org_models.Org).filter(org_models.Org.id == org_id)
    new_org = get_org.first()
    
    if new_org == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Org of id {org_id} not found')

    to_update = {}
    
    for key, value in request_org.items():
        if request_org[key] != None:
            if key == 'core_values' and new_org.core_values != None:
                to_update[key] = list(set(request_org[key] + new_org.core_values))
            else:
                to_update[key] = value
    
    to_update.update({"updated_date": date.today()})

    get_org.update(to_update, synchronize_session=False)
    db.commit()

    return new_org

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


####################################################

# Contact US CRUDs

# def create_message(org_id: int, message: contact_us_schemas.ContactMessageIn):

#     message_ids = []
#     new_message = message.dict()

#     for fakeMessage in fakeMessagesDb:
#         for key, value in fakeMessage.items():
#             if(key == 'id'):
#                 message_ids.append(value)

#     new_message.update({'id': int(message_ids[-1]) + 1, 'created_date': date.today(), 'status': 'new'})

#     fakeMessagesDb.append(new_message)
    
#     message = contact_us_schemas.ContactMessageOut(**new_message)

#     # print(fakeMessagesDb)

#     return message


# def get_messages(org_id: int, status: str, limit: int, offset: int):

#     messages = []

#     for fakeMessage in fakeMessagesDb:
#         for key, value in fakeMessage.items():
#             if key == 'status' and value == 'new' and org_id == org_id:
#                 messages.append(fakeMessage)

#     if len(messages) == 0:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No mesages found for the criteria provided")

#     return messages


