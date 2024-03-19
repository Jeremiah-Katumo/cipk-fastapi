from fastapi import FastAPI, status, HTTPException, UploadFile, File
from ..schemas import org_schemas
from datetime import datetime, date
from ..models import org_models
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List


def create_member(
    db: Session, 
    name: str, 
    image: UploadFile, 
    position: org_schemas.Positions, 
    social_media_links: List[str]
    ):
    return {"message": name}

