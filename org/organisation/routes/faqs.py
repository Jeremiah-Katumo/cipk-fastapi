from fastapi import FastAPI, status, HTTPException, Path, APIRouter
from typing import Annotated
# from ..schemas import schemas
# from ..cruds import cruds


router = APIRouter(
    prefix="/faqs",
    tags=['FAQs']
)


@router.get("/")
def get_all_faqs():
    return {'message': 'List of FAQs'}

@router.get("/{faq_id}")
def get_faq_item(faq_id: int):
    return {'message':'FAQs Item'}

@router.post('/')
def add_faq_item():
    return {'message': "FAQs Item Added"}

@router.patch("/")
def update_faq_item():
    return {'message': "FAQ Item Updated"}
