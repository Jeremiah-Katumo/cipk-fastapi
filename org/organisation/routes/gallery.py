from fastapi import FastAPI, status, HTTPException, Path, APIRouter
from typing import Annotated
from ..schemas import schemas
from ..cruds import cruds


router = APIRouter(
    prefix="/gallery",
    tags=['Gallery']
)


@router.get("/")
def get_all_gallery_items():
    return {'message': 'List of gallery items'}

@router.get("/{item_id}")
def get_gallery_item():
    return {'message':'Gallery Item'}

@router.post('/')
def add_gallery_item():
    return {'message': "Gallery Item Added"}

@router.patch("/")
def update_gallery_item():
    return {'message': "Gallery Item Updated"}