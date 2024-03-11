from fastapi import FastAPI, status, HTTPException
from . import schemas

fakeDB = [
    {
        'id': 1,
        'name': 'CIPK'
    }
]

def get_org(org_id: int):
    org = None 

    for db_org in fakeDB:
        for key, value in db_org.items():
            if(key == 'id' and value == org_id):
                org = db_org
                break
    return org

def create_org(org: schemas.OrgIn):
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

def update_org(org_id: int, org: schemas.OrgIn):
    
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