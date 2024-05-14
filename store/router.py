from fastapi import APIRouter
from store.controllers.products import router as product

api_router = APIRouter()
api_router.include_router(product, prefix="/products")