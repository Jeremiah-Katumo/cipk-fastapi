from fastapi import FastAPI, status, HTTPException, Path, APIRouter
from typing import Annotated
from .. import schemas, crud


router = APIRouter(
    prefix="/contact_us",
    tags=['Contact']
)

@router.post("/")
def contact_us():
    return {'message': 'Message sent'}


@router.get("/")
def get_messages():
    return {'message': 'User messages'}