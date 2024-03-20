from fastapi import FastAPI, status, HTTPException, UploadFile, File
from ..schemas import teams_schemas
from datetime import datetime, date
from ..models import org_models
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List
import os 
import uuid


def create_single_member(
    db: Session, 
    name: str, 
    org_id: int,
    profile_picture: str, 
    position: str, 
    social_media_links: str,
    phone: str,
    email: str
    ):
   
    get_member = db.query(org_models.TeamMember).filter(org_models.TeamMember.id == email)
    member_in_db = get_member.first()

    if member_in_db !=  None:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail=f'Member with email {email} already exists')

    db_member = org_models.TeamMember(
        name = name, 
        org_id = org_id,
        profile_picture = profile_picture, 
        position = position, 
        social_media_links = social_media_links,
        phone = phone,
        email = email,
        created_date = date.today()
    )
    db.add(db_member)
    db.commit()
    db.refresh(db_member)

    return db_member

def get_file_extension(profile_picture: UploadFile):
    filename = profile_picture.filename
    file_extension = filename.split('.')[-1]

    return file_extension

def hashed_filename_profile_picture(profile_picture: UploadFile):
    file_hash = uuid.uuid4()
    profile_picture.filename = f"{file_hash}.{get_file_extension(profile_picture)}"

    return profile_picture

def upload_file(org_id: int, member_id: int, profile_picture: UploadFile):

    # Deny uploads of types not png and jpeg/jpg
    allowed_extensions = ['png', 'jpg', 'jpeg']
    if get_file_extension(profile_picture).lower() not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Only png and jpg file formats are allowed")

    # Deny file uploads of gt 2 MB
    if profile_picture.size > 2000000: # 2 MB
        raise HTTPException(status_code=400, detail="Only files of size 2 MB or below are allowed")

    # Set the directory path
    org = f"org_{str(org_id)}"
    member = f"member_{str(member_id)}"
    profile_picture_image_path = os.path.join("org","organisation","images","profile_pictures",org,member)

    # Create directory path if missing
    if not os.path.exists(profile_picture_image_path):
        os.makedirs(profile_picture_image_path)

    full_file_path = os.path.join(profile_picture_image_path, profile_picture.filename)

    # Remove a file if already exists
    if os.path.exists(full_file_path):
        os.remove(full_file_path)

    # Put the new file
    with open(full_file_path, "wb") as image:
        image.write(profile_picture.file.read())

    # Return the uploaded file
    return profile_picture.filename


def create_member(
    db: Session, 
    name: str, 
    org_id: int,
    profile_picture: UploadFile, 
    position: teams_schemas.Positions, 
    social_media_links: List[str],
    phone: str = None,
    email: str = None
    ):

    # Update the UploadFile to have a hashed filename
    update_profile_picture = hashed_filename_profile_picture(profile_picture)
    new_file = update_profile_picture.filename 

    # Create the member record in DB
    new_member = create_single_member(
        db = db, 
        name = name, 
        org_id = org_id,
        profile_picture = new_file, 
        position = position, 
        social_media_links = social_media_links,
        phone =  phone,
        email = email
    )

    # Upload the profile photo
    upload_file(org_id, new_member.id, hashed_filename_profile_picture(profile_picture))

    # Return the upoloaded new member
    return new_member